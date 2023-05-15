# README: SP-Filters Repository
Welcome to the sp-filters repository! A database dedicated to maintaining and updating blocklists for our DNS Sinkhole Server.

## How it Works
The core of this repository is a Python code named blocklists.py. This script serves a crucial function - it combines data from two different text sources, one manually curated and the other automatically updated text source fetched from an external website.

These two sources are merged and updated in the output file, blocklists.txt. This allows us to maintain a comprehensive, continually updated blocklist that can effectively serve the needs of a DNS Sinkhole Server.

In addition to blocklists.py, we also have auto-source.py. This script is responsible for the automatic updating of the auto text source, ensuring real-time data is consistently available for blocklists.py.

## Project Goal
The mission with this project is to offer a dynamic approach to blocklist management for DNS Sinkhole Servers, mitigating the risks associated with malicious URLs, unwanted advertisements, and intrusive tracking/telemetry. By hosting and maintaining this project on GitHub, we also enable immediate, open-source updates to our database, further enhancing the capability and reliability of our solution.

Visit our repository [here](https://github.com/keanugithub/sp-filters) to learn more or contribute to our project.

