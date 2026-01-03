
# Broken Authentication Checker (API)

A lightweight Python tool to automatically identify **Broken Authentication**
issues in API **POST endpoints** by replaying requests from **Postman collections
exported as JSON**, without authentication.

---

## 🔍 Overview

Modern applications expose a large number of APIs through Postman collections.
Manually testing each POST endpoint for Broken Authentication is time-consuming
and does not scale.

This tool automates the initial security check by sending unauthenticated
requests to API endpoints and identifying those that still return successful
responses.

---

## 🎯 Problem Statement

If a sensitive API endpoint responds with `HTTP 200 OK` without valid
authentication, it indicates a **Broken Authentication** vulnerability
(OWASP API Top 10).

This tool helps security testers quickly identify such endpoints across large
API collections.

---

## ⚙️ How It Works

1. Export a Postman collection as a JSON file
2. Configure the target **base URL** inside the script
3. Run the tool with the exported JSON file
4. The tool:
   - Extracts POST API endpoints
   - Sends requests **without authentication headers**
   - Analyzes HTTP response codes
5. Endpoints responding with `200 OK` are flagged as potentially vulnerable

---

## 📥 Input: Postman Collection

### Exporting the Collection

1. Open Postman
2. Select the required API collection
3. Click **Export**
4. Save the file as `example.json`

This exported JSON file is used as input to the tool.

---

## 🌐 Base URL Configuration

Before running the script, configure the **base URL** inside
`broken_auth_check.py`.

Example:
```python
BASE_URL = "https://api.example.com/api1"
````

This allows testing different environments such as:

* Development
* Staging
* Testing

without modifying the Postman collection structure.

---

## ▶️ Usage

```bash
python3 broken_auth_check.py example.json
```

### Output

* Scan results are displayed in the terminal
* Potentially vulnerable endpoints are saved to `vulnerable.txt`

---

## 🧪 Example Output

```text
POST https://api.example.com/api1/user → 200 VULNERABLE
POST https://api.example.com/api1/login → 401 SECURE
```

---

## 📈 Scalability

Designed to handle **large Postman collections** containing hundreds of POST
API endpoints, making it suitable for real-world API security testing where
manual checks are impractical.

---

## 🛡️ Use Cases

* API penetration testing
* Application Security (AppSec) assessments
* SOC / Blue team API validation
* Bug bounty reconnaissance
* Pre-production security testing

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes and authorized security testing
only**. Do not use it against systems you do not own or have explicit permission
to test.

---

## 👨‍💻 Author

Vaidehi

```

---



