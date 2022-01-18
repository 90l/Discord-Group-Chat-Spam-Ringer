import json
import requests


with open('config.json') as f:
    config = json.load(f)

token = config.get('token')

amounts = int(input("How many requests do you want to make? \n"))


for _ in range(amounts):
            headers = {
            'Authorization': token,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.1011 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36'
            }
            requests.post('https://discord.com/api/v9/channels/923366115038617630/call/ring', headers=headers, json={"recipients":["913866260536762430","775637384812822528"]})


