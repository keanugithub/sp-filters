import requests
import base64
import os

# Assigning variables
GITHUB_API_URL = f"https://api.github.com/repos/keanugithub/sp-filters/contents/auto_source.txt"
GITHUB_HEADERS = {"Authorization": f"token {os.environ['SuperSecret']}"}
EXTERNAL_SOURCE = "https://big.oisd.nl/dnsmasq"

# Retrieve the current sha of the auto source file from GitHub
response = requests.get(GITHUB_API_URL, headers=GITHUB_HEADERS)

# Download the contents of the external URL source and encode to base64
new_contents = base64.b64encode(requests.get(EXTERNAL_SOURCE).content).decode()

# Update auto_source.txt and output to GitHub
data = {
    "message": "automatically updated",
    "content": new_contents,
    "branch": "main",
    "sha": response.json()["sha"]
} 
requests.put(GITHUB_API_URL, headers=GITHUB_HEADERS, json=data)
