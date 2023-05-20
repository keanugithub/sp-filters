import requests
import base64
import os

# Assigning variables
GITHUB_API_URL = f"https://api.github.com/repos/keanugithub/sp-filters/contents/auto_source.txt"
GITHUB_HEADERS = { "Authorization": f"token {os.environ['SuperSecret']}" }
EXTERNAL_URL_SOURCE = "https://big.oisd.nl/dnsmasq"

# Download the contents of the external URL source
response = requests.get(EXTERNAL_URL_SOURCE)
external_contents = response.content.decode().replace("server", "local")

# Retrieve the current sha of the auto source file from GitHub
current_sha = requests.get(GITHUB_API_URL, headers=GITHUB_HEADERS).json()["sha"]

# Encode the external contents to base64 format
new_contents = base64.b64encode(external_contents.encode()).decode()

# Update auto_source.txt
data = {
    "message": "auto-source updated by script",
    "content": new_contents,
    "branch": "main",
    "sha": current_sha
}

# Output to GitHub
requests.put(GITHUB_API_URL, headers=GITHUB_HEADERS, json=data)
