import os
import requests

# Assigning variables
GITHUB_API_URL = f"https://api.github.com/repos/keanugithub/sp-filters/contents/auto_source.txt"
GITHUB_HEADERS = { "Authorization": f"token {os.environ['SuperSecret']}" }
EXTERNAL_URL_SOURCE = "https://big.oisd.nl/dnsmasq"

# Download the contents of the external URL source
response = requests.get(EXTERNAL_URL_SOURCE)
contented = response.text.replace("server", "local")

# Update auto_source.txt
data = {
    "message": "auto-source updated by script",
    "content": contented,
    "branch": "main",
    }

# Output to GitHub
requests.put(GITHUB_API_URL, headers=GITHUB_HEADERS, json=data)
