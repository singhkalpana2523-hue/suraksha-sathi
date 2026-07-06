class ResponseBuilder:

    @staticmethod
    def build(result, metadata=None):

        details = result["analysis"]

        confidence = details.get("confidence", 0)

        if confidence >= 80:
            color = "red"
            recommendation = {
                "en": "Do NOT trust this message.",
                "hi": "इस संदेश पर भरोसा न करें।",
                "gu": "આ સંદેશ પર વિશ્વાસ ન કરો."
            }
            risk = "HIGH"

        elif confidence >= 50:
            color = "orange"
            recommendation = {
                "en": "Verify before taking action.",
                "hi": "कार्रवाई करने से पहले सत्यापित करें।",
                "gu": "કાર્ય કરતા પહેલાં ચકાસો."
            }
            risk = "MEDIUM"

        else:
            color = "green"
            recommendation = {
                "en": "Appears safe.",
                "hi": "यह सुरक्षित लगता है।",
                "gu": "આ સુરક્ષિત લાગે છે."
            }
            risk = "LOW"

        return {

            "status": "success",

            "input": {
                "type": metadata.get("input_type", "text")
            },

            "result": {

                "risk_level": risk,

                "risk_score": confidence,

                "color": color,

                "headline": details.get("scam_type"),

                # multilingual object
                "summary": details.get("summary"),

                "recommendation": recommendation

            },

            # multilingual lists
            "actions": details.get("action_steps", []),

            "red_flags": details.get("red_flags", []),

            "matched_patterns": details.get("matched_patterns", []),

            "metadata": metadata or {},

            "technical": result

        }