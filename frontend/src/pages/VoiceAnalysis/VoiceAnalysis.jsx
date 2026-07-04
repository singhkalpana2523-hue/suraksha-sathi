import { useState } from "react";

import PageHeader from "../../components/PageHeader/PageHeader";
import UploadArea from "../../components/UploadArea/UploadArea";
import Button from "../../components/Button/Button";
import EmptyState from "../../components/EmptyState/EmptyState";
import LoadingSpinner from "../../components/LoadingSpinner/LoadingSpinner";
import ResultCard from "../../components/ResultCard/ResultCard";

function VoiceAnalysis() {

  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [showResult, setShowResult] = useState(false);

  const handleAnalyze = () => {

    if (!file) {
      alert("Please upload an audio file first.");
      return;
    }

    setLoading(true);

    setTimeout(() => {
      setLoading(false);
      setShowResult(true);
    }, 3000);

  };

  return (
    <div className="min-h-screen bg-slate-950 text-white py-16">

      <div className="max-w-5xl mx-auto px-6">

        <PageHeader
          title="AI Voice Scam Analyzer"
          subtitle="Upload suspicious phone calls or voice messages for AI-powered scam detection."
        />

        <UploadArea
          file={file}
          setFile={setFile}
          accept="audio/*"
          title="🎤 Upload Voice Recording"
          subtitle="Upload MP3, WAV or M4A files"
        />

        {file && (

          <div className="mt-8">

            <audio
              controls
              className="w-full"
            >
              <source
                src={URL.createObjectURL(file)}
                type={file.type}
              />
              Your browser does not support audio.
            </audio>

          </div>

        )}

        <Button
          className="mt-8"
          onClick={handleAnalyze}
        >
          Analyze Voice
        </Button>

        {loading ? (

          <LoadingSpinner />

        ) : showResult ? (

          <ResultCard
            risk="Medium"
            score="7.8"
            category="Voice Phishing"
            confidence="92%"
            redFlags={[
              "Caller demanded urgent payment",
              "Threatening language detected",
              "Unknown phone number"
            ]}
            recommendations={[
              "Do not share OTP or bank details.",
              "Block the number.",
              "Report the incident."
            ]}
          />

        ) : (

          <EmptyState
            message="Upload a voice recording and click Analyze to generate an AI report."
          />

        )}

      </div>

    </div>
  );
}

export default VoiceAnalysis;