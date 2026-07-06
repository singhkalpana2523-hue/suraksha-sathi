import "./EmergencyCard.css";
import { useState } from "react";


export default function EmergencyCard({
    risk = "HIGH",
    result = null,
    onShare
}) {

const [showBanks, setShowBanks] = useState(false);



    const banks = [

        {
            name: "State Bank of India",
            url: "https://sbi.co.in"
        },

        {
            name: "HDFC Bank",
            url: "https://www.hdfcbank.com"
        },

        {
            name: "ICICI Bank",
            url: "https://www.icicibank.com"
        },

        {
            name: "Axis Bank",
            url: "https://www.axisbank.com"
        },

        {
            name: "Punjab National Bank",
            url: "https://www.pnbindia.in"
        },

        {
            name: "Bank of Baroda",
            url: "https://www.bankofbaroda.in"
        },

        {
            name: "Kotak Mahindra",
            url: "https://www.kotak.com"
        },

        {
            name: "Canara Bank",
            url: "https://canarabank.com"
        }

    ];

    const openCyberCrime = () => {

        window.open(
            "https://cybercrime.gov.in",
            "_blank"
        );

    };

    const call1930 = () => {

        window.location.href = "tel:1930";

    };

    


    const openBank = (url) => {

        window.open(url, "_blank");

    };

    return (

        <>

            <div className="emergency-section">

                <h2>

                    🚨 Emergency Help

                </h2>

                <div className="emergency-grid">

                    {

                        risk === "HIGH" &&

                        <div

                            className="emergency-card"

                            onClick={call1930}

                        >

                            <div className="emoji">

                                📞

                            </div>

                            <h3>

                                Call 1930

                            </h3>

                            <p>

                                National Cyber Fraud Helpline

                            </p>

                        </div>

                    }

                    {

                        risk !== "LOW" &&

                        <div

                            className="emergency-card"

                            onClick={openCyberCrime}

                        >

                            <div className="emoji">

                                🌐

                            </div>

                            <h3>

                                Cyber Crime

                            </h3>

                            <p>

                                Report Online

                            </p>

                        </div>

                    }

                    {

                        risk !== "LOW" &&

                        <div

                            className="emergency-card"

                            onClick={() => setShowBanks(true)}

                        >

                            <div className="emoji">

                                🏦

                            </div>

                            <h3>

                                Contact Bank

                            </h3>

                            <p>

                                Freeze Card / Account

                            </p>

                        </div>

                    }

                    <div

    className="emergency-card"

    onClick={onShare}
   


>

                        <div className="emoji">

                            📤

                        </div>

                        <h3>

    Share & Export

</h3>

<p>

    PDF • WhatsApp • Email

</p>
                    </div>

                </div>

            </div>

            {

                showBanks &&

                <div

                    className="bank-modal"

                    onClick={() => setShowBanks(false)}

                >

                    <div

                        className="bank-box"

                        onClick={(e) => e.stopPropagation()}

                    >

                        <h2>

                            🏦 Select Your Bank

                        </h2>

                        {

                            banks.map((bank) => (

                                <button

                                    key={bank.name}

                                    className="bank-btn"

                                    onClick={() => openBank(bank.url)}

                                >

                                    {bank.name}

                                </button>

                            ))

                        }
                        

                        <button

                            className="close-btn"

                            onClick={() => setShowBanks(false)}

                        >

                            Close

                        </button>
                        

                    </div>
                    

                </div>

            }
          

        </>

    );

}

    

