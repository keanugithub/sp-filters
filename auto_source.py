import os
import requests
import base64

# Assigning variables
GITHUB_BRANCH = "main"
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

# Encode the external contents to base64 format
encoded_contents = base64.b64encode(external_contents.encode()).decode()

# Update the file in the repository with the contents of the external URL source, only if the sha has changed
if encoded_contents != response_data["content"]:
    data = {
        "message": "Update auto_source from external URL",
        "content": encoded_contents,
        "branch": GITHUB_BRANCH,
        "sha": current_sha
    }
    response = requests.put(GITHUB_API_URL, headers=GITHUB_HEADERS, json=data)
