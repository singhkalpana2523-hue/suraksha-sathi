import "./WarningList.css";

export default function WarningList({
    warnings = [],
    language = "en"
}) {

    const heading = {
        en: "🚩 Warning Signs",
        hi: "🚩 चेतावनी संकेत",
        gu: "🚩 ચેતવણીના સંકેતો"
    };

    return (

        <div className="warning-section">

            <h2 className="warning-heading">
                {heading[language]}
            </h2>

            {
                warnings.length === 0 ? (

                    <p className="empty-text">
                        No warning signs detected.
                    </p>

                ) : (

                    <div className="warning-list">

                        {

                            warnings.map((warning, index) => (

                                <div
                                    key={index}
                                    className="warning-item"
                                >

                                    <span className="warning-icon">
                                        ⚠️
                                    </span>

                                    <span className="warning-text">
                                        {warning?.[language] || warning?.en}
                                    </span>

                                </div>

                            ))

                        }

                    </div>

                )

            }

        </div>

    );

}