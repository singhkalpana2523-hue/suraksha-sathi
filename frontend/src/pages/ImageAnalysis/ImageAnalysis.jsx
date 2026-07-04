import { useState } from "react";

import PageHeader from "../../components/PageHeader/PageHeader";
import UploadArea from "../../components/UploadArea/UploadArea";
import Button from "../../components/Button/Button";
import EmptyState from "../../components/EmptyState/EmptyState";
import LoadingSpinner from "../../components/LoadingSpinner/LoadingSpinner";

function ImageAnalysis() {

  const [file, setFile] = useState(null);
const [loading, setLoading] = useState(false);
const [showResult, setShowResult] = useState(false);
const handleAnalyze = () => {

  if (!file) {
    alert("Please upload an image first.");
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
          title="AI Image Scam Analyzer"
          subtitle="Upload screenshots, QR codes and suspicious images to detect online scams."
        />

       <UploadArea
  file={file}
  setFile={setFile}
  accept="image/*"
  title="📷 Upload Image"
  subtitle="Drag & Drop or Click to Browse"
/>

        {file && (

          <div className="mt-8">

            <img

              src={URL.createObjectURL(file)}

              alt="Preview"

              className="rounded-2xl border border-slate-700 w-full max-h-[450px] object-contain"

            />

          </div>

        )}

        <Button
  className="mt-8"
  onClick={handleAnalyze}
>
  Analyze Image
</Button>

 {loading ? (

  <LoadingSpinner />

) : showResult ? (

  <ResultCard
    risk="High"
    score="9.2"
    category="QR Code Scam"
    confidence="95%"
    redFlags={[
      "Suspicious QR code detected",
      "Unknown website",
      "Payment request"
    ]}
    recommendations={[
      "Do not scan the QR code.",
      "Verify the sender.",
      "Report suspicious content."
    ]}
  />

) : (

  <EmptyState
    message="Upload an image and click Analyze to generate an AI report."
  />

)}

      </div>

    </div>

  );

}

export default ImageAnalysis;