import requests
import base64
import json
import os

# naming assignments
GITHUB_BRANCH = "main"
GITHUB_TOKEN = os.environ['SuperSecret']
GITHUB_REPO_URL = "https://api.github.com/repos/keanugithub/sp-filters/contents/blocklists.txt"
GITHUB_FILE_URL = "https://raw.githubusercontent.com/keanugithub/sp-filters/main/blocklists.txt"

MANUAL_SOURCE_URL = "https://raw.githubusercontent.com/keanugithub/sp-filters/main/manual_source.txt"
AUTO_SOURCE_URL = "https://raw.githubusercontent.com/keanugithub/sp-filters/main/auto_source.txt"

# fetch latest manual and auto sources
manual_source = requests.get(MANUAL_SOURCE_URL).text.strip()
auto_source = requests.get(AUTO_SOURCE_URL).text.strip()

# combine sources with current content of blocklists.txt
response = requests.get(GITHUB_FILE_URL, headers={"Authorization": "Token " + os.environ['SuperSecret']})
content = response.text.strip()

new_content = f"[----------MANUAL SOURCE----------]\n\n{manual_source}\n\n[----------AUTO SOURCE----------]\n\n{auto_source}\n{content}"

# update blocklists.txt on GitHub
data = {
    "message": "blocklists updated by script",
    "content": base64.b64encode(new_content.encode()).decode(),
    "sha": response.json()["sha"],
    "branch": GITHUB_BRANCH
}
response = requests.put(GITHUB_REPO_URL, headers={"Authorization": "Token " + os.environ['SuperSecret']}, data=json.dumps(data))