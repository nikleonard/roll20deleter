import http.client
import requests
import json
headers = {
    'authority': "app.roll20.net",
    'accept': "application/json, text/javascript, */*; q=0.01",
    'accept-language': "en-US,en;q=0.9,es;q=0.8",
    'cookie': "",
    'referer': "https://app.roll20.net/audio_library/",
    'sec-ch-ua': "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': "\"Windows\"",
    'sec-fetch-dest': "empty",
    'sec-fetch-mode': "cors",
    'sec-fetch-site': "same-origin",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    'x-requested-with': "XMLHttpRequest"
}
url = "https://app.roll20.net/audio_library/search?alltracks=true"
response = requests.get(url, headers=headers)
data = response.text
json_data = json.loads(data)
if 'tracks' in json_data:
    for track in json_data['tracks']:
        trackdata = json.loads(track)
        print(trackdata['id'])
        url = "https://app.roll20.net/audio_library/delete/" + str(trackdata['id'])
        try:
            response = requests.post(url, headers=headers, timeout=1)
            data = response.text
            print(data)
        except requests.exceptions.Timeout:
            print("The request timed out for track: " + str(trackdata['id']))
