import requests
import base64
import json
import os

GITHUB_BRANCH = "main"
TOKEN = os.environ['TOKEN']
GITHUB_REPO_URL = "https://api.github.com/repos/keanugithub/sp-filters/contents/blocklists.txt"
MANUAL_SOURCE_URL = "https://raw.githubusercontent.com/keanugithub/sp-filters/main/manual_source"
AUTO_SOURCE_URL = "https://raw.githubusercontent.com/keanugithub/sp-filters/main/auto_source"

# fetch blocklists.txt content
response = requests.get(GITHUB_REPO_URL + "?ref=" + GITHUB_BRANCH, headers={"Authorization": "Token " + os.environ['TOKEN']})
content = base64.b64decode(response.json()["content"]).decode()

# fetch latest manual and auto sources
manual_source = requests.get(MANUAL_SOURCE_URL).text.strip()
auto_source = requests.get(AUTO_SOURCE_URL).text.strip()

# combine sources with blocklists.txt content
new_content = f"[----------MANUAL SOURCE----------]\n\n{manual_source}\n\n[----------AUTO SOURCE----------]\n\n{auto_source}\n{content}"

# update blocklists.txt on GitHub
data = {
    "message": "script auto update",
    "content": base64.b64encode(new_content.encode()).decode(),
    "sha": response.json()["sha"],
    "branch": GITHUB_BRANCH
}
response = requests.put(GITHUB_REPO_URL, headers={"Authorization": "Token " + os.environ['TOKEN']}, data=json.dumps(data))

print("success")