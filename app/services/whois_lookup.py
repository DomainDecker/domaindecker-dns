import whois

def fetch_whois(domain: str) -> dict:
    try:
        w = whois.whois(domain)
        return dict(w)
    except Exception as e:
        return {"error": str(e)}
