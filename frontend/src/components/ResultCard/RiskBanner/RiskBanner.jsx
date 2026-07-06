import "./RiskBanner.css";

export default function RiskBanner({ risk }) {

    const banner = {

        HIGH: {
            emoji: "🚨",
            title: "SCAM DETECTED",
            color: "high"
        },

        MEDIUM: {
            emoji: "⚠️",
            title: "SUSPICIOUS MESSAGE",
            color: "medium"
        },

        LOW: {
            emoji: "✅",
            title: "SAFE MESSAGE",
            color: "low"
        }

    };

    const current = banner[risk] || banner.LOW;

    return (

        <div className={`risk-banner ${current.color}`}>

            <span className="risk-icon">

                {current.emoji}

            </span>

            <span className="risk-title">

                {current.title}

            </span>

        </div>

    );

}