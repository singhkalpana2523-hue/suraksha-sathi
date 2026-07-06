import "./LanguageSwitcher.css";

export default function LanguageSwitcher({
    language,
    setLanguage
}) {

    const languages = [

        {
            code: "en",
            flag: "🇬🇧",
            label: "English"
        },

        {
            code: "hi",
            flag: "🇮🇳",
            label: "हिन्दी"
        },

        {
            code: "gu",
            flag: "🇮🇳",
            label: "ગુજરાતી"
        }

    ];

    return (

        <div className="language-section">

            <h2 className="language-heading">

                🌐 Language

            </h2>

            <div className="language-buttons">

                {

                    languages.map((lang) => (

                        <button

                            key={lang.code}

                            onClick={() => setLanguage(lang.code)}

                            className={
                                language === lang.code
                                    ? "language-btn active"
                                    : "language-btn"
                            }

                        >

                            <span>

                                {lang.flag}

                            </span>

                            {lang.label}

                        </button>

                    ))

                }

            </div>

        </div>

    );

}