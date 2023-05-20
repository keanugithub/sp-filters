import requests
import base64
import os

# Assigning variables
GITHUB_API_URL = f"https://api.github.com/repos/keanugithub/sp-filters/contents/auto_source.txt"
GITHUB_HEADERS = { "Authorization": f"token {os.environ['SuperSecret']}" }
EXTERNAL_URL_SOURCE = "https://big.oisd.nl/dnsmasq"

# Update auto_source.txt
response = requests.get(GITHUB_API_URL, headers=GITHUB_HEADERS)
data = {
    "message": "auto-source updated by script",
    "content": base64.b64encode(requests.get(EXTERNAL_URL_SOURCE).content.decode().replace("server", "local").encode()).decode(),
    "branch": "main",
    "sha": response.json()["sha"]
}

# Output to GitHub
requests.put(GITHUB_API_URL, headers=GITHUB_HEADERS, json=data)
