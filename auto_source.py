import requests
import base64
import os

# Assigning variables
GITHUB_API_URL = f"https://api.github.com/repos/keanugithub/sp-filters/contents/auto_source.txt"
GITHUB_HEADERS = { "Authorization": f"token {os.environ['SuperSecret']}" }
EXTERNAL_URL_SOURCE = "https://big.oisd.nl/dnsmasq"

# Download the contents of the external URL source
external_contents = requests.get(EXTERNAL_URL_SOURCE).content.decode().replace("server", "local")

# Update auto_source.txt and commit message
data = {
    "message": "auto-source updated by script",
    "content": base64.b64encode(external_contents.encode()).decode(),
    "branch": "main"
}

# Retrieve SHA to ensure update
current_sha = requests.get(GITHUB_API_URL, headers=GITHUB_HEADERS).json()["sha"]
data["sha"] = current_sha

# Output to GitHub
requests.put(GITHUB_API_URL, headers=GITHUB_HEADERS, json=data)
