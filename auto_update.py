import requests
import base64
import json

GITHUB_BRANCH = "main"
GITHUB_TOKEN = "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"
print(GITHUB_TOKEN)
GITHUB_REPO_URL = "https://api.github.com/repos/keanugithub/sp-filters/contents/blocklists.txt"
MANUAL_SOURCE_URL = "https://raw.githubusercontent.com/keanugithub/sp-filters/main/manual_source"
AUTO_SOURCE_URL = "https://raw.githubusercontent.com/keanugithub/sp-filters/main/auto_source"

# fetch blocklists.txt content
response = requests.get(GITHUB_REPO_URL + "?ref=" + GITHUB_BRANCH, headers={"Authorization": "Token " + GITHUB_TOKEN})
print(response.json())
content = base64.b64decode(response.json()["content"]).decode()

# fetch latest manual and auto sources
manual_source = requests.get(MANUAL_SOURCE_URL).text.strip()
auto_source = requests.get(AUTO_SOURCE_URL).text.strip()

# combine sources with blocklists.txt content
new_content = f"{manual_source}\n{auto_source}\n{content}"

# update blocklists.txt on GitHub
data = {
    "message": "Update blocklists.txt",
    "content": base64.b64encode(new_content.encode()).decode(),
    "sha": response.json()["sha"],
    "branch": GITHUB_BRANCH
}
response = requests.put(GITHUB_REPO_URL, headers={"Authorization": "Token " + GITHUB_TOKEN}, data=json.dumps(data))

print(success)