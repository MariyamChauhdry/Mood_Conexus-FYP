# 🎭 Mood Conexus – Emotion-Based Anime & Book Recommender

**Mood Conexus** is an intelligent web-based application that detects a user's real-time facial emotion and recommends **anime** and **books** based on that emotional state.

---

## 🧠 Final Year Project Overview

This project uses real-time facial emotion recognition to understand a user's mood and recommend content accordingly. Whether a user is feeling **sad**, **happy**, **angry**, or **surprised** — the system responds with emotionally aligned anime and book suggestions.

---

## 🚀 Features

- 🎥 Real-Time Emotion Detection using webcam  
- 📚 Content-Aware Recommendation System  
- 📖 Recommends Books & Anime based on:  
  - Detected Emotion  
  - User Preferences  
- ❤️ Favorite System (with Firebase)  
- 📈 User-friendly Interface with Live Previews  
- 🔒 Firebase Authentication  

---

## 🛠️ Tech Stack

| Frontend | Backend | Database | ML/AI |
|----------|---------|----------|-------|
| React (Vite + Tailwind CSS) | Flask (Python) | Firebase Firestore | Face API, Emotion Model, Recommender System |

---

## 🧬 Emotion Flow Logic

1. The user comes in front of the camera  
2. Face API detects facial features & emotion  
3. Detected emotion (e.g., *sad*) is stored in Firebase  
4. Flask backend fetches emotion → queries Firestore for matching books/anime  
5. Recommendations are displayed to the user  

---

## 🧪 How to Run Locally

### 📦 Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### 🧠 Backend Setup (Flask)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### 🔐 Firebase Configuration

- Add your Firebase credentials in these files:
  - `frontend/src/firebase.js`
  - `backend/firebase_config.py`
  - `Groq API`
- These are **ignored** in Git for security.

---

## 📸 Screenshots

### 🏠 Home Page
![Home](https://github.com/MariyamChauhdry/Mood_Conexus-FYP/blob/main/frontend/public/home.png?raw=true)

---

### 📺 Default Anime Page
![Default Anime](https://github.com/MariyamChauhdry/Mood_Conexus-FYP/blob/main/frontend/public/defualtanime.png?raw=true)

---

### 📚 Default Book Page
![Default Book](https://github.com/MariyamChauhdry/Mood_Conexus-FYP/blob/main/frontend/public/defualtbook.png?raw=true)

---

### ℹ️ About Page
![About](https://github.com/MariyamChauhdry/Mood_Conexus-FYP/blob/main/frontend/public/about.png?raw=true)

---

### 📬 Contact Page
![Contact](https://github.com/MariyamChauhdry/Mood_Conexus-FYP/blob/main/frontend/public/contact.png?raw=true)

---

### 🤖 Emotion Detection Page
![Emotion Detection](https://github.com/MariyamChauhdry/Mood_Conexus-FYP/blob/main/frontend/public/emotiondetection.png?raw=true)

---

### ❤️ Favorite Anime Page
![Favorite Anime](https://github.com/MariyamChauhdry/Mood_Conexus-FYP/blob/main/frontend/public/fav.png?raw=true)

---

### 📘 Favorite Book Page
![Favorite Book](https://github.com/MariyamChauhdry/Mood_Conexus-FYP/blob/main/frontend/public/favbook.png?raw=true)

---

### 🎭 Anime Recommendation Page
![Anime Recommendation](https://github.com/MariyamChauhdry/Mood_Conexus-FYP/blob/main/frontend/public/animerecommendation.png?raw=true)

---

### 📖 Book Recommendation Page
![Book Recommendation](https://github.com/MariyamChauhdry/Mood_Conexus-FYP/blob/main/frontend/public/bookrecommendation.png?raw=true)

---

### 💬 MoodConexus Assistant
![ChatBot](https://github.com/MariyamChauhdry/Mood_Conexus-FYP/blob/main/frontend/public/chatbot.png?raw=true)

---

## 📊 Dataset Information

- Collected anime and book data using **web scraping**  
- Each entry includes: title, description, genre, rating, and emotion tag  
- Data is stored in Firebase Firestore  
- Emotions include: `happy`, `sad`, `angry`, `surprised`, `fear`, `neutral`, `disgust`.

---

## 📚 Use Case & Importance

> In an emotionally aware digital world, **Mood Conexus** enhances user engagement by recommending content that resonates with the user's **current mental state**.

This technology can be used in:
- 📱 Entertainment platforms  
- 🧘 Mental health apps  
- 👩‍🏫 Educational content filtering  
- 🧠 Emotion-aware AI systems

---

## 🙋‍♀️ About Me

**👩‍💻 Mariyam Chauhdry**  
AI Engineer  
GitHub: [@MariyamChauhdry](https://github.com/MariyamChauhdry)

---

## 🏁 Conclusion

**Mood Conexus** blends **real-time emotion recognition**, **intelligent recommendations**, and **modern UI** to deliver a personalized digital experience.

It demonstrates the power of combining:  
- Machine Learning (emotion models)  
- Full Stack Web Development (React + Flask)  
- Cloud Services (Firebase)  

to solve real-world problems with empathy and intelligence.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
