import { useState } from "react";
import LoadingSpinner from "../../components/LoadingSpinner/LoadingSpinner";
import Button from "../../components/Button/Button";
import ResultCard from "../../components/ResultCard/ResultCard";
import UploadArea from "../../components/UploadArea/UploadArea";
import PageHeader from "../../components/PageHeader/PageHeader";
import EmptyState from "../../components/EmptyState/EmptyState";


function TextAnalysis() {

const [text, setText] = useState("");
const [loading, setLoading] = useState(false);
const [showResult, setShowResult] = useState(false);
const handleAnalyze = () => {

  if (text.trim() === "") {
    alert("Please enter a suspicious message first.");
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

        {/* Heading */}

        <PageHeader
    title="AI Text Scam Analyzer"
    subtitle="Analyze suspicious SMS, Emails, WhatsApp messages and social media conversations using AI."
/>

        <p className="text-center text-slate-400 mt-5 text-lg">

          Analyze suspicious SMS, Emails, WhatsApp messages and social media chats.

        </p>

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

  <ResultCard
    risk="High"
    score="9.5"
    category="Phishing"
    confidence="96%"
    redFlags={[
      "Urgent payment request",
      "Suspicious URL",
      "Unknown sender"
    ]}
    recommendations={[
      "Do not click suspicious links.",
      "Block the sender.",
      "Report to cybercrime.gov.in"
    ]}
  />

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