import os
import requests

# Assigning variables
GITHUB_BRANCH = "main"
GITHUB_API_URL = f"https://api.github.com/repos/keanugithub/sp-filters/contents/auto_source"
GITHUB_HEADERS = { "Authorization": f"token {os.environ['SuperSecret']}" }
EXTERNAL_URL_SOURCE = "https://big.oisd.nl/dnsmasq"

# Download the contents of the external URL source
response = requests.get(EXTERNAL_URL_SOURCE)
external_contents = response.content.decode()

# Update the file in the repository with the contents of the external URL source
data = {
    "message": "Update auto_source from external URL",
    "content": external_contents,
    "branch": GITHUB_BRANCH
}
response = requests.put(GITHUB_API_URL, headers=GITHUB_HEADERS, json=data)