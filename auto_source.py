import requests
import base64
import os

# Assigning variables
GITHUB_API_URL = f"https://api.github.com/repos/keanugithub/sp-filters/contents/auto_source.txt"
GITHUB_HEADERS = {"Authorization": f"token {os.environ['SuperSecret']}"}
EXTERNAL_SOURCE = "https://big.oisd.nl/dnsmasq"

# Retrieve the current sha of the auto source file from GitHub
response = requests.get(GITHUB_API_URL, headers=GITHUB_HEADERS)

# uownload the contents of the external URL source and decode to base64
new_contents = requests.get(EXTERNAL_URL_SOURCE).content.decode().replace("server", "local")

# update auto_source.txt and output to GitHub
data = {
    "message": "automatically updated",
    "content": base64.b64encode(new_contents.encode()).decode(),
    "branch": "main",
    "sha": response.json()["sha"]
} 
requests.put(GITHUB_API_URL, headers=GITHUB_HEADERS, json=data)
