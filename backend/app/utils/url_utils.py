import ipaddress
import re
from urllib.parse import urlparse


SHORTENERS = {
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "goo.gl",
    "ow.ly",
    "cutt.ly",
    "rb.gy",
    "is.gd"
}


BANK_KEYWORDS = {
    "bank",
    "upi",
    "paytm",
    "phonepe",
    "gpay",
    "googlepay",
    "sbi",
    "icici",
    "hdfc",
    "axis",
    "kotak",
    "yesbank"
}


SUSPICIOUS_TLDS = {
    ".xyz",
    ".top",
    ".click",
    ".loan",
    ".zip",
    ".review",
    ".country",
    ".win"
}

TRUSTED_BRANDS = {
    "google": [
        "google.com",
        "accounts.google.com"
    ],

    "amazon": [
        "amazon.in",
        "amazon.com"
    ],

    "sbi": [
        "sbi.co.in",
        "onlinesbi.sbi"
    ],

    "paytm": [
        "paytm.com"
    ],

    "phonepe": [
        "phonepe.com"
    ],

    "hdfc": [
        "hdfcbank.com"
    ],

    "icici": [
        "icicibank.com"
    ]
}


def get_domain(url: str):

    parsed = urlparse(url)

    return parsed.netloc.lower()


def is_ip(domain: str):

    try:

        ipaddress.ip_address(domain)

        return True

    except Exception:

        return False


def is_shortener(domain: str):

    return domain in SHORTENERS


def contains_bank_keyword(url: str):

    url = url.lower()

    return any(word in url for word in BANK_KEYWORDS)


def suspicious_tld(domain: str):

    return any(domain.endswith(tld) for tld in SUSPICIOUS_TLDS)


def url_length(url: str):

    return len(url)


def hyphen_count(url: str):

    return url.count("-")


def dot_count(domain: str):

    return domain.count(".")


def has_login_keywords(url: str):

    keywords = [
        "login",
        "verify",
        "update",
        "secure",
        "signin",
        "account"
    ]

    url = url.lower()

    return any(word in url for word in keywords)


def contains_credentials(url: str):

    parsed = urlparse(url)

    return "@" in parsed.netloc


def contains_punycode(domain: str):

    return "xn--" in domain


def excessive_encoding(url: str):

    return len(re.findall(r"%[0-9A-Fa-f]{2}", url)) > 5
def detect_brand_impersonation(domain: str):

    domain = domain.lower()

    for brand, trusted_domains in TRUSTED_BRANDS.items():

        if brand in domain:

            if not any(domain.endswith(td) for td in trusted_domains):

                return True, brand

    return False, None