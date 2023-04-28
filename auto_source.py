import os
import requests
import base64

# Assigning variables
GITHUB_BRANCH = "main"
GITHUB_API_URL = f"https://api.github.com/repos/keanugithub/sp-filters/contents/auto_source.txt"
GITHUB_HEADERS = { "Authorization": f"token {os.environ['SuperSecret']}" }
EXTERNAL_URL_SOURCE = "https://big.oisd.nl/dnsmasq"

# Download the contents of the external URL source
response = requests.get(EXTERNAL_URL_SOURCE)
external_contents = response.content.decode()

# Encode the contents of the external URL source
encoded_contents = base64.b64encode(external_contents.encode()).decode()

# Update the file in the repository with the encoded contents of the external URL source
data = {
    "message": "auto_source updated by script",
    "content": encoded_contents,
    "branch": GITHUB_BRANCH
}
response = requests.put(GITHUB_API_URL, headers=GITHUB_HEADERS, json=data)
