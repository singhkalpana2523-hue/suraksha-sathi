import { useState } from "react";

import PageHeader from "../../components/PageHeader/PageHeader";
import UploadArea from "../../components/UploadArea/UploadArea";
import Button from "../../components/Button/Button";
import EmptyState from "../../components/EmptyState/EmptyState";
import LoadingSpinner from "../../components/LoadingSpinner/LoadingSpinner";
import ResultCard from "../../components/ResultCard/ResultCard";
import { analyzeVoice } from "../../services/analysisService";

function VoiceAnalysis() {

  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [showResult, setShowResult] = useState(false);
  const [result, setResult] = useState(null);

  const handleAnalyze = async () => {

  if (!file) {
    alert("Please upload an audio file first.");
    return;
  }

  setLoading(true);

  try {

    const response = await analyzeVoice(file);

    setResult(response);

    setShowResult(true);

  } catch(err) {

    console.error(err);
    alert("Voice analysis failed.");

  } finally {

    setLoading(false);

  }

};

  return (
    <div className="min-h-screen bg-slate-950 text-white py-16">

      <div className="max-w-5xl mx-auto px-6">

        <PageHeader
          title="Voice Scam Analyzer"
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

          <ResultCard result={result} />

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