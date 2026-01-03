import json
import sys
import requests

# ---- Argument check ----
if len(sys.argv) != 2:
    print("Usage: python3 tool.py postman.json")
    sys.exit(1)

postman_file = sys.argv[1]

# ---- Load Postman JSON ----
with open(postman_file, "r") as f:
    data = json.load(f)

# ---- Extract endpoints ----
def extract_endpoints(data):
    endpoints = []
    items = data.get("item", [])

    for item in items:
        if "request" in item:
            method = item["request"].get("method")
            url = item["request"].get("url", {})
            raw_url = url.get("raw")

            endpoints.append({
                "method": method,
                "url": raw_url
            })

    return endpoints

# ---- Send request without auth ----
def send_request_no_auth(method, url):
    try:
        r = requests.request(method, url, timeout=10)
        return r.status_code
    except Exception as e:
        print("Error requesting:", url)
        return None

# ---- Decide vulnerability ----
def check_broken_auth(status_code):
    if status_code == 200:
        return "VULNERABLE"
    elif status_code in [401, 403]:
        return "SECURE"
    else:
        return "REVIEW"

# ---- Main logic ----
endpoints = extract_endpoints(data)
vulnerable = []

for ep in endpoints:
    status = send_request_no_auth(ep["method"], ep["url"])
    result = check_broken_auth(status)

    print(ep["method"], ep["url"], "→", status, result)

    if result == "VULNERABLE":
        vulnerable.append(ep)

# ---- Save vulnerable endpoints ----
with open("vulnerable.txt", "w") as f:
    for v in vulnerable:
        f.write(f"{v['method']} {v['url']}\n")

print("\nScan complete.")
print("Vulnerable endpoints saved to vulnerable.txt")
