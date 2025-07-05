from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import re
from joblib import dump, load
import logging
from chat import chat_bp

app = Flask(__name__)
CORS(app)
# Configure logging to see detailed console output
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load and preprocess datasets
def load_data():
    
    anime_df = pd.read_excel('anime_with_emotions.xlsx').dropna()
    book_df = pd.read_excel('book_dataset.xlsx').dropna()
    
    # Clean and standardize data
    anime_df['emotion'] = anime_df['emotion'].str.lower().str.strip()
    book_df['emotion'] = book_df['emotion'].str.lower().str.strip()
    
    emotion_map = {
        'surprised': 'surprise',
        'fearful': 'fear',
        'angry': 'anger',
        'disgust': 'disgust'
        # Add other mappings as needed
    }
    
    anime_df['emotion'] = anime_df['emotion'].str.lower().str.strip().map(emotion_map).fillna(anime_df['emotion'])
    book_df['emotion'] = book_df['emotion'].str.lower().str.strip().map(emotion_map).fillna(book_df['emotion'])
    
    # Create combined features for better recommendations
    anime_df['features'] = (
        anime_df['title'].astype(str) + " " +
        anime_df['description'].astype(str) + " " +
        anime_df['genre'].astype(str)
    )
    
    book_df['features'] = (
        book_df['title'].astype(str) + " " +
        book_df['description'].astype(str) + " " +
        book_df['emotion_based_genre'].astype(str)
    )
    
    return anime_df, book_df

anime_df, book_df = load_data()

# Initialize and train TF-IDF vectorizers
def initialize_models():
    # Create model directory if not exists
    os.makedirs('models', exist_ok=True)
    
    try:
        # Try loading pre-trained models
        anime_vectorizer = load('models/anime_vectorizer.joblib')
        book_vectorizer = load('models/book_vectorizer.joblib')
        anime_tfidf = load('models/anime_tfidf.joblib')
        book_tfidf = load('models/book_tfidf.joblib')
    except:
        # Train new models if loading fails
        anime_vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
        book_vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
        
        anime_tfidf = anime_vectorizer.fit_transform(anime_df['features'])
        book_tfidf = book_vectorizer.fit_transform(book_df['features'])
        
        # Save models
        dump(anime_vectorizer, 'models/anime_vectorizer.joblib')
        dump(book_vectorizer, 'models/book_vectorizer.joblib')
        dump(anime_tfidf, 'models/anime_tfidf.joblib')
        dump(book_tfidf, 'models/book_tfidf.joblib')
    
    return anime_vectorizer, book_vectorizer, anime_tfidf, book_tfidf

anime_vectorizer, book_vectorizer, anime_tfidf, book_tfidf = initialize_models()

# Recommendation Engine
class RecommendationEngine:
    def __init__(self, df, vectorizer, tfidf_matrix):
        self.df = df
        self.vectorizer = vectorizer
        self.tfidf_matrix = tfidf_matrix
        self.emotion_indices = {
            emotion: df[df['emotion'] == emotion].index 
            for emotion in df['emotion'].unique()
        }
        self.emotion_map = {
            'surprised': 'surprise',
            'fearful': 'fear',
            'angry': 'anger'
        }
    
    def get_recommendations(self, emotion, top_n=15, min_similarity=0.2):
        try:
            # Standardize emotion input
            emotion = emotion.lower().strip()
            emotion = self.emotion_map.get(emotion, emotion)
            
            # Get items that actually match the requested emotion
            emotion_items = self.df[self.df['emotion'] == emotion]
            if len(emotion_items) == 0:
                print(f"No items found for emotion: {emotion}")
                return []

            # Calculate average vector for emotion-matched items
            emotion_indices = emotion_items.index
            emotion_vectors = self.tfidf_matrix[emotion_indices]
            avg_vector = np.mean(emotion_vectors, axis=0)
            
            # Convert to numpy array and reshape
            avg_vector_array = np.asarray(avg_vector).reshape(1, -1)
            tfidf_matrix_array = np.asarray(self.tfidf_matrix.todense())
            
            # Calculate similarities with all items
            similarities = cosine_similarity(avg_vector_array, tfidf_matrix_array)
            similarities = similarities.flatten()
            
            # Create DataFrame for filtering and sorting
            rec_df = self.df.copy()
            rec_df['similarity_score'] = similarities
            
            # Filter and sort recommendations
            recommendations = (
                rec_df
                # Exclude items that already have this emotion
                .loc[~rec_df.index.isin(emotion_indices)]
                # Filter by minimum similarity threshold
                .query(f"similarity_score >= {min_similarity}")
                # Sort by similarity score descending
                .sort_values('similarity_score', ascending=False)
            )
            recommendations = recommendations.sample(n=min(top_n, len(recommendations)), random_state=np.random.randint(0, 10000)).to_dict('records')

            
            return recommendations

        except Exception as e:
            print(f"Recommendation error: {str(e)}")
            import traceback
            traceback.print_exc()
            return []

# Initialize recommendation engines
anime_engine = RecommendationEngine(anime_df, anime_vectorizer, anime_tfidf)
book_engine = RecommendationEngine(book_df, book_vectorizer, book_tfidf)

@app.route('/')
def index():
    return {"message": "Mood Conexus API is running."}

app.register_blueprint(chat_bp)

# API Endpoints
@app.route('/api/emotion', methods=['POST'])
def handle_emotion():
    # Log that we received a request
    logger.debug("\n=== Received Emotion Detection Request ===")
    data = request.get_json()
    logger.debug(f"Raw emotion data received: {data}")
    emotion = data.get('emotion', '').lower().strip()
    
    if not emotion:
        return jsonify({'status': 'error', 'message': 'Emotion parameter is required'}), 400
    
    # Standardize the emotion
    emotion_map = {
            'surprised': 'surprise',
            'fearful': 'fear',
            'angry': 'anger'
        }
    raw_emotion = data['emotion'].lower().strip()
    processed_emotion = emotion_map.get(raw_emotion, raw_emotion)
        
    logger.debug(f"Processing: {raw_emotion} -> {processed_emotion}")
    
    # Get recommendations
    anime_recs = anime_engine.get_recommendations(processed_emotion)
    book_recs = book_engine.get_recommendations(processed_emotion)
    # Log the results before sending back
    logger.debug(f"Generated {len(anime_recs)} anime recommendations")
    logger.debug(f"Generated {len(book_recs)} book recommendations")
    def truncate_description(desc, max_lines=3, max_length=300):
        """Clean and truncate description to specified number of lines and characters"""
        if not desc:
            return ""
            
        # Clean the description first
        clean_desc = desc.replace('_x000D_\n', '\n').strip()
        
        # Truncate by lines
        lines = [line.strip() for line in clean_desc.split('\n') if line.strip()]
        truncated = '\n'.join(lines[:max_lines])
        
        # Further truncate by character length if needed
        if len(truncated) > max_length:
            truncated = truncated[:max_length].rsplit(' ', 1)[0] + "..."
        elif len(lines) > max_lines:
            truncated += "..."
            
        return truncated
    
    # Format responses
    def format_anime(anime):
        return {
            'title': anime.get('title', ''),
            'rating': float(anime.get('rating', 0)),
            'description': truncate_description(anime.get('description', '')),
            'thumbnail': anime.get('thumbnail', ''),
            'previewlink': anime.get('previewlink', ''),
            'emotion': anime.get('emotion', ''),
            'genre': anime.get('genre', ''),
            'similarity_score': float(anime.get('similarity_score', 0))
        }
    
    def format_book(book):
        return {
            'title': book.get('title', ''),
            'rating': float(book.get('rating', 0)),
            'description': truncate_description(book.get('description', '')),
            'thumbnail': book.get('thumbnail', ''),
            'previewlink': book.get('previewLink', ''),
            'emotion': book.get('emotion', ''),
            'genre': book.get('emotion_based_genre', book.get('genre', '')),
            'similarity_score': float(book.get('similarity_score', 0))
        }

    return jsonify({
        'status': 'success',
        'emotion': emotion,
        'anime_recommendations': [format_anime(a) for a in anime_recs],
        'book_recommendations': [format_book(b) for b in book_recs]
    })

@app.route('/api/available_emotions', methods=['GET'])
def get_available_emotions():
    return jsonify({
        'anime_emotions': sorted(anime_df['emotion'].unique()),
        'book_emotions': sorted(book_df['emotion'].unique())
    })

if __name__ == '__main__':
   
    print("\n=== MoodConexus Backend Starting ===")
    print("Available emotions:")
    print(f"Anime: {sorted(anime_df['emotion'].unique())}")
    print(f"Books: {sorted(book_df['emotion'].unique())}")
    print("Server running on http://localhost:5000")
    print("Waiting for emotion data from frontend...\n")
    app.run(host='0.0.0.0', port=5000, debug=True)