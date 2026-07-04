from app.models.url_models import URLAnalysisResponse
from app.utils.url_utils import (
    get_domain,
    is_ip,
    is_shortener,
    contains_bank_keyword,
    suspicious_tld,
    url_length,
    hyphen_count,
    dot_count,
    has_login_keywords,
    contains_credentials,
    contains_punycode,
    excessive_encoding,
    
)


class URLService:

    def analyze(self, url: str) -> URLAnalysisResponse:

        score = 0

        reasons = []

        detected = []

        domain = get_domain(url)

        # -----------------------------
        # Rule 1 : HTTPS
        # -----------------------------
        if not url.startswith("https://"):
            score += 20
            reasons.append("Uses HTTP instead of HTTPS.")
            detected.append("HTTP")

        # -----------------------------
        # Rule 2 : IP Address
        # -----------------------------
        if is_ip(domain):
            score += 30
            reasons.append("Uses an IP address instead of a domain.")
            detected.append("IP Address")

        # -----------------------------
        # Rule 3 : URL Shortener
        # -----------------------------
        if is_shortener(domain):
            score += 20
            reasons.append("Uses a URL shortening service.")
            detected.append("Shortened URL")

        # -----------------------------
        # Rule 4 : Banking Keywords
        # -----------------------------
        if contains_bank_keyword(url):
            score += 20
            reasons.append("Contains banking/payment related keywords.")
            detected.append("Bank Keywords")

        # -----------------------------
        # Rule 5 : Suspicious Login Words
        # -----------------------------
        if has_login_keywords(url):
            score += 10
            reasons.append("Contains login/verify/update keywords.")
            detected.append("Login Keywords")

        # -----------------------------
        # Rule 6 : Very Long URL
        # -----------------------------
        if url_length(url) > 100:
            score += 10
            reasons.append("URL is unusually long.")
            detected.append("Long URL")

        # -----------------------------
        # Rule 7 : Too Many Hyphens
        # -----------------------------
        if hyphen_count(url) >= 3:
            score += 10
            reasons.append("URL contains multiple hyphens.")
            detected.append("Hyphens")

        # -----------------------------
        # Rule 8 : Too Many Subdomains
        # -----------------------------
        if dot_count(domain) >= 3:
            score += 10
            reasons.append("Contains many subdomains.")
            detected.append("Subdomains")

        # -----------------------------
        # Rule 9 : Suspicious TLD
        # -----------------------------
        if suspicious_tld(domain):
            score += 20
            reasons.append("Suspicious top-level domain.")
            detected.append("Suspicious TLD")

        # -----------------------------
        # Rule 10 : Hidden Credentials
        # -----------------------------
        if contains_credentials(url):
            score += 25
            reasons.append("Contains embedded credentials.")
            detected.append("Credentials")

        # -----------------------------
        # Rule 11 : Punycode
        # -----------------------------
        if contains_punycode(domain):
            score += 30
            reasons.append("Uses Punycode domain.")
            detected.append("Punycode")

        # -----------------------------
        # Rule 12 : Excessive Encoding
        # -----------------------------
        if excessive_encoding(url):
            score += 15
            reasons.append("Contains excessive URL encoding.")
            detected.append("Encoding")

        # -----------------------------
        # Limit Score
        # -----------------------------
        score = min(score, 100)

        # -----------------------------
        # Risk Level
        # -----------------------------
        if score >= 70:
            risk = "High"

        elif score >= 40:
            risk = "Medium"

        else:
            risk = "Low"

        return URLAnalysisResponse(

            url=url,

            risk_score=score,

            risk_level=risk,

            is_suspicious=score >= 40,

            reasons=reasons,

            detected_features=detected

        )