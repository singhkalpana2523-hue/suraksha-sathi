from app.services.url_service import URLService

service = URLService()

urls = [

    "https://google.com",

    "https://www.sbi.co.in",

    "http://secure-sbi-login.xyz",

    "https://bit.ly/payment",

    "http://192.168.0.10/login",

    "https://amaz0n.in",

    "https://xn--oogle-qmc.com",

    "https://secure-bank-login-update.xyz"

]

for url in urls:

    result = service.analyze(url)

    print("=" * 60)

    print("URL:", url)

    print("Risk:", result.risk_level)

    print("Score:", result.risk_score)

    print("Reasons:")

    for reason in result.reasons:
        print("-", reason)

    print()