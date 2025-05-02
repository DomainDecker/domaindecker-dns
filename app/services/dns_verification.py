import dns.resolver

def verify_txt(domain: str, verification: str) -> bool:
    try:
        subdomain = f"_domaindecker.verification.{domain}"
        answers = dns.resolver.resolve(subdomain, "TXT")
        for rdata in answers:
            for txt_string in rdata.strings:
                if isinstance(txt_string, bytes):
                    txt_string = txt_string.decode()
                if txt_string.strip() == verification:
                    return True
        return False
    except Exception:
        return False
