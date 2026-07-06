import { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar/Navbar";

import Home from "./pages/Home/Home";
import TextAnalysis from "./pages/TextAnalysis/TextAnalysis";
import ImageAnalysis from "./pages/ImageAnalysis/ImageAnalysis";
import VoiceAnalysis from "./pages/VoiceAnalysis/VoiceAnalysis";
import History from "./pages/History/History";
import About from "./pages/About/About";
import Login from "./pages/Login/Login";
import Signup from "./pages/Signup/Signup";
import Profile from "./pages/Profile/Profile";

function App() {

  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <BrowserRouter>

      <Navbar
        isLoggedIn={isLoggedIn}
        setIsLoggedIn={setIsLoggedIn}
      />

      <Routes>

        <Route path="/" element={<Home />} />

        <Route
          path="/login"
          element={
            <Login
              setIsLoggedIn={setIsLoggedIn}
            />
          }
        />

        <Route path="/signup" element={<Signup />} />

        <Route path="/text-analysis" element={<TextAnalysis />} />
        <Route path="/image-analysis" element={<ImageAnalysis />} />
        <Route path="/voice-analysis" element={<VoiceAnalysis />} />
        <Route path="/history" element={<History />} />
        <Route path="/about" element={<About />} />
        <Route path="/profile" element={<Profile />} />

      </Routes>

    </BrowserRouter>
  );
}

export default App;