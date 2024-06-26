import requests
import base64
import json
import os

# naming assignments
GITHUB_HEADERS = {"Authorization": "Token " + os.environ['SuperSecret']}
GITHUB_FILE_URL = "https://api.github.com/repos/keanugithub/sp-filters/contents/blocklists.txt"
MANUAL_SOURCE_URL = "https://raw.githubusercontent.com/keanugithub/sp-filters/main/manual_source.txt"
AUTO_SOURCE_URL = "https://raw.githubusercontent.com/keanugithub/sp-filters/main/auto_source.txt"

# fetch latest manual and auto sources
manual_source = requests.get(MANUAL_SOURCE_URL).text.strip()
auto_source = requests.get(AUTO_SOURCE_URL).text.strip()

# create new content by combining sources
new_content = f"#[----------MANUAL SOURCE----------]\n\n{manual_source}\n\n#[----------AUTO SOURCE----------]\n\n{auto_source}"

# get current content of blocklists.txt and decode
response = requests.get(GITHUB_FILE_URL + "?ref=main", headers=GITHUB_HEADERS)
current_content = base64.b64decode(response.json()["content"]).decode()

# update and encode contents to blocklists.txt then output to GitHub
data = {
    "message": "automatically updated",
    "content": base64.b64encode(new_content.encode()).decode(),
    "branch": "main",
    "sha": response.json()["sha"]    
} 
requests.put(GITHUB_FILE_URL, headers=GITHUB_HEADERS, data=json.dumps(data))
