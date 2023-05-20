import os
import requests
import base64

# Assigning variables
GITHUB_API_URL = f"https://api.github.com/repos/keanugithub/sp-filters/contents/auto_source.txt"
GITHUB_HEADERS = {"Authorization": f"token {os.environ['SuperSecret']}"}
EXTERNAL_URL_SOURCE = "https://big.oisd.nl/dnsmasq"

# Retrieve the current sha of the auto source file from GitHub
response = requests.get(GITHUB_API_URL, headers=GITHUB_HEADERS)
current_sha = response.json()["sha"]

# Download the contents of the external URL source and encode to base64
external_contents = base64.b64encode(requests.get(EXTERNAL_URL_SOURCE).content).decode()

# Update auto_source.txt and output to GitHub
data = {
    "message": "auto-source updated by script",
    "content": external_contents,
    "branch": "main",
    "sha": current_sha
}
requests.put(GITHUB_API_URL, headers=GITHUB_HEADERS, json=data)
