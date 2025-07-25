import { Provider } from "react-redux";
import Home from "./components/Home/Home";
import Login from "./components/login/Login";
import Register from "./components/register/Register";
import About from "./components/About/About";
import store from "../src/components/Redux/store";
import Contact from "./components/Contact/Contact";
import Capture from "./components/Capture/Capture";
import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";
import { useState } from "react";
import Favorites from "./components/Favorite/Favorite";
import Chatbot from "./components/Chatbot/Chatbot";
//import Test from "./components/test/test";
import { useSelector } from "react-redux";

function App() {
  return (
    <Provider store={store}>
      <BrowserRouter>
        <AppContent />
      </BrowserRouter>
    </Provider>
  );
}

function AppContent() {
  const location = useLocation();
  const [theme, setTheme] = useState("purple");
  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);

  const showChatbotRoutes = ["/home", "/contact", "/about", "/favorites"];
  const shouldShowChatbot = isAuthenticated && showChatbotRoutes.includes(location.pathname);

  const changeTheme = () => {
    if (theme === "purple") {
      setTheme("blue");
    } else if (theme === "blue") {
      setTheme("grey");
    } else if (theme === "grey") {
      setTheme("green");
    } else if (theme === "green") {
      setTheme("red");
    } // else if (theme === "red") {
    //   setTheme("pink");
    //       }
      else {
      setTheme("purple");
    }
  };

  return (
    <>
      {shouldShowChatbot && <Chatbot />}
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/home" element={<Home theme={theme} changeTheme={changeTheme} />} />
        <Route path="/register" element={<Register />} />
        {/* <Route path="/test" element={<Test />} /> */}
        <Route path="/login" element={<Login />} />
        <Route path="/about" element={<About theme={theme} changeTheme={changeTheme} />} />
        <Route path="/contact" element={<Contact theme={theme} changeTheme={changeTheme} />} />
        <Route path="/capture" element={<Capture />} />
        <Route path="/favorites" element={<Favorites />} />
        
      </Routes>
    </>
  );
}

export default App;
