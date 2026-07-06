import "./ActionList.css";

export default function ActionList({
    actions = [],
    language = "en"
}) {

    const heading = {
        en: "✅ What You Should Do",
        hi: "✅ आपको क्या करना चाहिए",
        gu: "✅ હવે શું કરવું"
    };

    return (

        <div className="action-section">

            <h2 className="action-heading">
                {heading[language]}
            </h2>

            {

                actions.length === 0 ? (

                    <p className="empty-text">
                        No recommended actions.
                    </p>

                ) : (

                    <div className="action-list">

                        {

                            actions.map((action, index) => (

                                <div
                                    key={index}
                                    className="action-item"
                                >

                                    <span className="action-icon">
                                        ✔️
                                    </span>

                                    <span className="action-text">
                                        {action?.[language] || action?.en}
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