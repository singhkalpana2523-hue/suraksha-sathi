import { useState } from "react";

import PageHeader from "../../components/PageHeader/PageHeader";
import UploadArea from "../../components/UploadArea/UploadArea";
import Button from "../../components/Button/Button";
import EmptyState from "../../components/EmptyState/EmptyState";
import LoadingSpinner from "../../components/LoadingSpinner/LoadingSpinner";
import ResultCard from "../../components/ResultCard/ResultCard";

import { analyzeQR } from "../../services/analysisService";

function QRAnalysis() {

    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const [showResult, setShowResult] = useState(false);
    const [result, setResult] = useState(null);

    const handleAnalyze = async () => {

        if (!file) {
            alert("Please upload a QR image first.");
            return;
        }

        setLoading(true);

        try {

            const response = await analyzeQR(file);

            setResult(response);

            setShowResult(true);

        } catch (error) {

            console.error(error);

            alert("QR Analysis failed.");

        } finally {

            setLoading(false);

        }

    };

    return (

        <div className="min-h-screen bg-slate-950 text-white py-16">

            <div className="max-w-5xl mx-auto px-6">

                <PageHeader
                    title="AI QR Scam Analyzer"
                    subtitle="Upload payment or website QR codes to detect malicious links and scam attempts."
                />

                <UploadArea
                    file={file}
                    setFile={setFile}
                    accept="image/*"
                    title="📱 Upload QR Code"
                    subtitle="Upload a QR Code image"
                />

                {file && (

                    <div className="mt-8">

                        <img
                            src={URL.createObjectURL(file)}
                            alt="QR Preview"
                            className="rounded-2xl border border-slate-700 w-full max-h-[450px] object-contain"
                        />

                    </div>

                )}

                <Button
                    className="mt-8"
                    onClick={handleAnalyze}
                >
                    Analyze QR
                </Button>

                {loading ? (

                    <LoadingSpinner />

                ) : showResult ? (

                    <ResultCard result={result} />

                ) : (

                    <EmptyState
                        message="Upload a QR Code and click Analyze."
                    />

                )}

            </div>

        </div>

    );

}

export default QRAnalysis;