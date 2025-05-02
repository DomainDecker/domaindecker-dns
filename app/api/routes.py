from fastapi import APIRouter, Query
from app.services.whois_lookup import fetch_whois
from app.services.dns_verification import verify_txt

router = APIRouter()

@router.get("/whois/{domain}")
def whois_lookup(domain: str):
    return fetch_whois(domain)

@router.get("/verify-txt/{domain}")
def verify_txt_record(domain: str, verification: str = Query(..., description="TXT record verification value")):
    verified = verify_txt(domain, verification)
    return {"verified": verified}
