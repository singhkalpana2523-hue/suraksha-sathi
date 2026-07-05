class ResponseBuilder:

    @staticmethod
    def build(result, metadata=None):

        details = result["analysis"]

        confidence = details.get("confidence", 0)

        if confidence >= 80:
            color = "red"
            recommendation = "🚫 Do NOT trust this message."
            risk = "HIGH"

        elif confidence >= 50:
            color = "orange"
            recommendation = "⚠ Verify before taking action."
            risk = "MEDIUM"

        else:
            color = "green"
            recommendation = "✅ Appears safe."
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

                "summary": details.get("summary"),

                "recommendation": recommendation

            },

            "actions": details.get(
                "recommended_actions",
                []
            ),

            "red_flags": details.get(
                "red_flags",
                []
            ),

            "matched_patterns": details.get(
                "matched_patterns",
                []
            ),

            "metadata": metadata or {},

            "technical": {

                "provider": result.get("provider"),

                "model": result.get("model"),

                "response_time_ms": result.get(
                    "response_time_ms"
                ),

                "analysis": details

            }

        }