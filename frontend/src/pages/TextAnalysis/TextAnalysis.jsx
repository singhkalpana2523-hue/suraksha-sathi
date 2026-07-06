import { useState } from "react";
import LoadingSpinner from "../../components/LoadingSpinner/LoadingSpinner";
import Button from "../../components/Button/Button";
import ResultCard from "../../components/ResultCard/ResultCard";
import UploadArea from "../../components/UploadArea/UploadArea";
import PageHeader from "../../components/PageHeader/PageHeader";
import EmptyState from "../../components/EmptyState/EmptyState";
import { analyzeText } from "../../services/analysisService";


function TextAnalysis() {

const [text, setText] = useState("");
const [loading, setLoading] = useState(false);
const [showResult, setShowResult] = useState(false);
const [result, setResult] = useState(null);
const handleAnalyze = async () => {

  if (text.trim() === "") {
    alert("Please enter a suspicious message first.");
    return;
  }

  setLoading(true);

  try {

    const response = await analyzeText(text);

    setResult(response);

    setShowResult(true);

  } catch (err) {

    console.error(err);
    alert("Analysis failed.");

  } finally {

    setLoading(false);

  }

};

  return (

    <div className="min-h-screen bg-slate-950 text-white py-16">

      <div className="max-w-5xl mx-auto px-6">

        {/* Heading */}

        <PageHeader
    title="Text Scam Analyzer"
    subtitle="Analyze suspicious SMS, Emails, WhatsApp messages and social media conversations using AI."
/>

         

        {/* Input Section */}

        <div className="bg-slate-900 rounded-2xl border border-slate-800 p-8 mt-14">

          <h2 className="text-2xl font-semibold mb-5">

            Paste Suspicious Message

          </h2>

          <textarea

            rows="12"

            value={text}

            onChange={(e) => setText(e.target.value)}

            placeholder="Paste the suspicious message here..."

            className="w-full bg-slate-950 border border-slate-700 rounded-xl p-5 outline-none focus:border-cyan-400 resize-none"

          />

         <Button
  className="mt-6"
  onClick={handleAnalyze}
>
  Analyze Message
</Button>
         {loading ? (

  <LoadingSpinner />

) : showResult ? (

  <ResultCard result={result} />

) : (

  <EmptyState
    message="Paste a suspicious message and click Analyze to generate an AI report."
  />

)}



        </div>

      </div>

    </div>

  );

}

export default TextAnalysis;