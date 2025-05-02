# DomainDecker TXT + Whois API (FastAPI)

A lightweight, production-ready FastAPI backend for **DomainDecker**. This service enables users to:

- **Verify domain ownership** via DNS TXT records.
- **Fetch domain registration details** using WHOIS data.

## Project Structure

```
domain-decker-backend/
├── app/
│   ├── main.py                # FastAPI application entry point
│   ├── api/
│   │   └── routes.py          # API route definitions
│   ├── services/
│   │   ├── dns_verification.py # TXT record verification logic
│   │   └── whois_lookup.py     # WHOIS lookup logic
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/domain-decker-backend.git
   cd domain-decker-backend
   ```

2. **Create and activate a virtual environment** (recommended):

   ```bash
   python -m venv venv
   # On Unix/macOS:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

**Start the FastAPI server:**

```bash
uvicorn app.main:app --reload
```

Server will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## API Endpoints

### 🔍 WHOIS Lookup

- **Endpoint:** `GET /whois/{domain}`
- **Description:** Returns full WHOIS data for the specified domain.

### ✅ TXT Record Verification

- **Endpoint:** `GET /verify-txt/{domain}`
- **Query Parameter:** `verification` (the expected TXT value)
- **Description:** Verifies that the domain contains a TXT record under `_domaindecker.verification.{domain}` with the provided value.

#### Example

```bash
curl "http://127.0.0.1:8000/verify-txt/example.com?verification=abc123xyz"
```

**Response:**

```json
{
  "verified": true
}
```

---

## Credits

- Inspired by [FastAPI](https://fastapi.tiangolo.com/) and [Uvicorn](https://www.uvicorn.org/).
- WHOIS functionality may use [python-whois](https://pypi.org/project/python-whois/) or similar libraries.
- DNS verification logic may use [dnspython](https://www.dnspython.org/).
- Project maintained by [Elisha Smile](https://github.com/elishasmil3).
