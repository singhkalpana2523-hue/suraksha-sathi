import "./SummaryCard.css";

export default function SummaryCard({
    title,
    summary,
    language = "en"
}) {

    const headings = {
        en: "📝 Why is this Dangerous?",
        hi: "📝 यह खतरनाक क्यों है?",
        gu: "📝 આ કેમ જોખમી છે?"
    };

    return (
        <div className="summary-container">

            <h2 className="summary-title">
                {title}
            </h2>

            <div className="summary-box">

                <h3 className="summary-heading">
                    {headings[language]}
                </h3>

                <p className="summary-text">
                    {summary?.[language] || summary?.en || "No summary available."}
                </p>

            </div>

        </div>
    );
}