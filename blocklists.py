import requests
import base64
import json
import os

# naming assignments
GITHUB_BRANCH = "main"
GITHUB_TOKEN = os.environ['SuperSecret']
GITHUB_FILE_URL = "https://api.github.com/repos/keanugithub/sp-filters/contents/blocklists.txt"

MANUAL_SOURCE_URL = "https://raw.githubusercontent.com/keanugithub/sp-filters/main/manual_source.txt"
AUTO_SOURCE_URL = "https://raw.githubusercontent.com/keanugithub/sp-filters/main/auto_source.txt"

# fetch latest manual and auto sources
manual_source = requests.get(MANUAL_SOURCE_URL).text.strip()
auto_source = requests.get(AUTO_SOURCE_URL).text.strip()

# create new content by combining sources
new_content = f"[----------MANUAL SOURCE----------]\n\n{manual_source}\n\n[----------AUTO SOURCE----------]\n\n{auto_source}"

# get current content of blocklists.txt from GitHub
response = requests.get(GITHUB_FILE_URL + "?ref=" + GITHUB_BRANCH, headers={"Authorization": "Token " + os.environ['SuperSecret']})
current_content = base64.b64decode(response.json()["content"]).decode()

# update blocklists.txt
data = {
    "message": "blocklists updated by script",
    "content": base64.b64encode(new_content.encode()).decode(),
    "sha": response.json()["sha"],
    "branch": GITHUB_BRANCH
}
response = requests.put(GITHUB_FILE_URL, headers={"Authorization": "Token " + os.environ['SuperSecret']}, data=json.dumps(data))
