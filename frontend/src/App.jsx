import { BrowserRouter, Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar/Navbar";

import Home from "./pages/Home/Home";
import TextAnalysis from "./pages/TextAnalysis/TextAnalysis";
import ImageAnalysis from "./pages/ImageAnalysis/ImageAnalysis";
import VoiceAnalysis from "./pages/VoiceAnalysis/VoiceAnalysis";
import History from "./pages/History/History";
import About from "./pages/About/About";

function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/text-analysis" element={<TextAnalysis />} />
        <Route path="/image-analysis" element={<ImageAnalysis />} />
        <Route path="/voice-analysis" element={<VoiceAnalysis />} />
        <Route path="/history" element={<History />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;