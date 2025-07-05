// import { useNavigate } from "react-router-dom";

// const Test = () => {
//   const navigate = useNavigate();

//   return (
//     <div className="min-h-screen flex flex-col justify-center items-center bg-gray-900 text-white">
//       <h1 className="text-3xl font-bold mb-6">This is a New Page</h1>
//       <button
//         onClick={() => navigate("/")}
//         className="px-6 py-3 bg-purple-600 hover:bg-purple-500 text-white font-semibold rounded-xl shadow-lg transition"
//       >
//         Go Back to Mood Conexus
//       </button>
//     </div>
//   );
// };

// export default Test;

//COUNTER COMPONENT
// import { useState } from 'react';

// const EvaluationPage = () => {
//   const [clickCount, setClickCount] = useState(0);

//   return (
//     <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center p-4">
//       <h1 className="text-3xl font-bold mb-8">FYP Evaluation Page</h1>
//       <div className="bg-purple-950 rounded-lg p-8 max-w-md w-full text-center">
//         <p className="mb-6">Click the button to count:</p>
        
//         {/* Counter display */}
//         <div className="text-4xl font-mono mb-6">
//           {clickCount}
//         </div>
        
//         {/* Counting button */}
//         <button
//           onClick={() => setClickCount(prev => prev + 1)}
//           className="bg-purple-600 hover:bg-purple-500 text-white px-8 py-3 rounded-lg text-xl font-medium transition-colors"
//         >
//           Click Me
//         </button>
//       </div>
//     </div>
//   );
// };

// export default EvaluationPage;

import { Link } from 'react-router-dom';

const EvaluationPage = () => {
  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center p-4">
      <h1 className="text-3xl font-bold mb-8">FYP Evaluation Page</h1>
      
        <p className="mb-6">This is the Final Year Project.</p>
        
        <Link 
          to="/" 
          className="bg-purple-600 hover:bg-purple-500 text-white px-6 py-2 rounded-lg text-lg font-medium transition-colors"
        >
          Return to Mood Conexus
        </Link>
      
    </div>
  );
};

export default EvaluationPage;