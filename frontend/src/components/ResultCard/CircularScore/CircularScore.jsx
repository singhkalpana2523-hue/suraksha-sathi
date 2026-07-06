import "./CircularScore.css";
import { useEffect, useState } from "react";

export default function CircularScore({

    score = 0,

    risk = "LOW"

}) {

    const [progress, setProgress] = useState(0);

    useEffect(() => {

        let current = 0;

        const timer = setInterval(() => {

            current++;

            if (current >= score) {

                current = score;
                clearInterval(timer);

            }

            setProgress(current);

        }, 15);

        return () => clearInterval(timer);

    }, [score]);



    const radius = 90;

    const stroke = 14;

    const normalizedRadius = radius - stroke / 2;

    const circumference = normalizedRadius * 2 * Math.PI;

    const strokeDashoffset =
        circumference -
        (progress / 100) * circumference;



    let color = "#22c55e";

    let glow = "rgba(34,197,94,.55)";

    let label = "SAFE";

    let emoji = "✅";



    if (risk === "MEDIUM") {

        color = "#f59e0b";

        glow = "rgba(245,158,11,.55)";

        label = "MEDIUM RISK";

        emoji = "⚠️";

    }



    if (risk === "HIGH") {

        color = "#ef4444";

        glow = "rgba(239,68,68,.60)";

        label = "HIGH RISK";

        emoji = "🚨";

    }



    return (

        <div className="score-container">

            <svg
    className="progress-ring"
    width="260"
    height="260"
    viewBox="0 0 220 220"
>

                <circle

                    className="progress-bg"

                    stroke="#263349"

                    strokeWidth={stroke}

                    fill="transparent"

                    r={normalizedRadius}

                    cx="110"

                    cy="110"

                />



                <circle

                    className="progress-bar"

                    stroke={color}

                    strokeWidth={stroke}

                    strokeLinecap="round"

                    fill="transparent"

                    r={normalizedRadius}

                    cx="110"

                    cy="110"

                    strokeDasharray={circumference}

                    strokeDashoffset={strokeDashoffset}

                    style={{
    filter: `
        drop-shadow(0 0 12px ${glow})
        drop-shadow(0 0 24px ${glow})
        drop-shadow(0 0 40px ${glow})
    `
}}

                />

            </svg>



            <div className="score-content">

                <div className="score-number">

                    {progress}<span>%</span>

                </div>

                <div className="score-title">

                    Scam Probability

                </div>

                <div
                    className="score-risk"
                    style={{ color }}
                >

                    {emoji} {label}

                </div>

            </div>

        </div>

    );

}