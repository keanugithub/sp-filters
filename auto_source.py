import os
import requests
import base64

# Assigning variables
GITHUB_API_URL = f"https://api.github.com/repos/keanugithub/sp-filters/contents/auto_source.txt"
GITHUB_HEADERS = { "Authorization": f"token {os.environ['SuperSecret']}" }
EXTERNAL_URL_SOURCE = "https://big.oisd.nl/dnsmasq"

# Retrieve the current sha of the auto source file from GitHub
response = requests.get(GITHUB_API_URL, headers=GITHUB_HEADERS)
response_data = response.json()
current_sha = response_data["sha"]

# Download the contents of the external URL source
response = requests.get(EXTERNAL_URL_SOURCE)
external_contents = response.content.decode()
external_contents = external_contents.replace("server", "local")

# Encode the external contents to base64 format
encoded_contents = base64.b64encode(external_contents.encode()).decode()

# Update auto_source.txt
data = {
    "message": "auto-source updated by script",
    "content": encoded_contents,
    "branch": "main",
    "sha": current_sha }
response = requests.put(GITHUB_API_URL, headers=GITHUB_HEADERS, json=data)
