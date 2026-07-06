class ResponseBuilder:

    @staticmethod
    def build(result, metadata=None):

        details = result["analysis"]

        classification = (
            details.get("classification", "SAFE")
            .upper()
            .strip()
        )

        confidence = details.get("confidence", 0)

        # ---------------------------------------
        # SAFE
        # ---------------------------------------
        if classification == "SAFE":

            risk = "LOW"
            risk_score = max(0, 100 - confidence)
            color = "green"

            recommendation = {
                "en": "This appears to be a legitimate website/message.",
                "hi": "यह एक वैध वेबसाइट/संदेश प्रतीत होता है।",
                "gu": "આ માન્ય વેબસાઇટ/સંદેશ લાગે છે."
            }

        # ---------------------------------------
        # SUSPICIOUS
        # ---------------------------------------
        elif classification == "SUSPICIOUS":

            risk = "MEDIUM"
            risk_score = max(confidence, 50)
            color = "orange"

            recommendation = {
                "en": "Verify before taking action.",
                "hi": "कार्रवाई करने से पहले सत्यापित करें।",
                "gu": "કાર્ય કરતા પહેલાં ચકાસો."
            }

        # ---------------------------------------
        # SCAM
        # ---------------------------------------
        else:

            risk = "HIGH"
            risk_score = confidence
            color = "red"

            recommendation = {
                "en": "Do NOT trust this message.",
                "hi": "इस संदेश पर भरोसा न करें।",
                "gu": "આ સંદેશ પર વિશ્વાસ ન કરો."
            }

        return {

            "status": "success",

            "input": {
                "type": metadata.get("input_type", "text")
            },

            "result": {

                "risk_level": risk,

                "risk_score": risk_score,

                "color": color,

                "headline": details.get("scam_type"),

                "summary": details.get("summary"),

                "recommendation": recommendation

            },

            "actions": details.get("action_steps", []),

            "red_flags": details.get("red_flags", []),

            "matched_patterns": details.get("matched_patterns", []),

            "metadata": metadata or {},

            "technical": result

        }