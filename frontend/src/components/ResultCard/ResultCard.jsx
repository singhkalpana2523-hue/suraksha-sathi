import "./ResultCard.css";

import { useState } from "react";

import RiskBanner from "./RiskBanner/RiskBanner";
import CircularScore from "./CircularScore/CircularScore";
import SummaryCard from "./SummaryCard/SummaryCard";
import WarningList from "./WarningList/WarningList";
import ActionList from "./ActionList/ActionList";
import LanguageSwitcher from "./LanguageSwitcher/LanguageSwitcher";
import EmergencyCard from "./EmergencyCard/EmergencyCard";
import ShareModal from "./ShareModal/ShareModal";

export default function ResultCard({ result }) {

    const [language, setLanguage] = useState("en");
    const [showShare, setShowShare] = useState(false);

    if (!result) return null;

    const risk = result.result?.risk_level || "LOW";

    const summary =
    result.result?.summary || {};

    const warnings =
    result.red_flags ??
    result.result?.red_flags ??
    [];

const actions =
    result.actions ??
    result.result?.actions ??
    [];

    return (

        <div className="result-container">

            <RiskBanner

                risk={risk}

                title={result.result.headline}

            />

            <div className="result-top">

                <CircularScore

                    score={result.result.risk_score}

                    risk={risk}

                />

            </div>

            <LanguageSwitcher

                language={language}

                setLanguage={setLanguage}

            />

            <SummaryCard
    title={result.result.headline}
    summary={summary}
    language={language}
/>

            <WarningList

                warnings={warnings}

                language={language}

            />

            <ActionList

                actions={actions}

                language={language}

            />
        <EmergencyCard
    risk={risk}
    result={result}
    onShare={() => setShowShare(true)}
/>

<ShareModal
    open={showShare}
    onClose={() => setShowShare(false)}
    result={result}
/>

        </div>

    );

}