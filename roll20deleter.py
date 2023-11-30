import http.client
import requests
import json
headers = {
    'authority': "app.roll20.net",
    'accept': "application/json, text/javascript, */*; q=0.01",
    'accept-language': "en-US,en;q=0.9,es;q=0.8",
    'cookie': "gdpr_accepts_cookies=true; _fbp=fb.1.1630637260688.820802525; __stripe_mid=1b0ac13c-fc3c-40d7-9b96-100a07261fb3dc9393; __stripe_mid=5bfc154d-874e-41bd-bf8d-083e6ead6238041c25; _tt_enable_cookie=1; _ttp=e1b69f2f-c143-46ee-a9b6-1b4ddcb304b0; _rdt_uuid=1683681420272.b0073fbd-440e-412e-96ce-2bf69e7209da; _ga_1111=GS1.1.1690756213.4.0.1690756213.0.0.0; cf_clearance=FT_Qx.S2e7CosBNooUwlMJc9GnJ8LrEgiti5c2uOcak-1692892453-0-1-570b95c5.dc3eaa56.aca25-160.0.0; _gcl_au=1.1.957354066.1695928891; fs_uid=#10GVRN#7d3091dd-5b8f-4324-94cd-228bc7f9a1cc:b2d4cb4c-aebe-439a-805f-f7eac30ad271:1699999812634::2#2cefb68a#/1721005268; rack.session=45ba8e0ed731650deaa44ffbb0c09374afba2d286840eb245a8fc3a74cbbbbf7; _gid=GA1.2.112953115.1701366140; _clck=1e7xr8r%7C2%7Cfh5%7C0%7C1292; __hstc=175753277.ecc465c15173a31612d6a5bc3ec23f83.1701366569651.1701366569651.1701366569651.1; hubspotutk=ecc465c15173a31612d6a5bc3ec23f83; __hssrc=1; _conv_v=vi%3A1*sc%3A22*cs%3A1701366140*fs%3A1692493051*pv%3A38*exp%3A%7B100410420.%7Bv.100431275-g.%7B10049424.1-10049425.1-10049428.1%7D%7D-100410426.%7Bv.100431287-g.%7B10049424.1-10049425.1-10049428.1%7D%7D-100413749.%7Bv.100438939-g.%7B10049424.1-10049425.1-10049428.1%7D%7D%7D*ps%3A1699999812; roll20tempauth=51; _uetsid=cfb85a308fa711eebc77d7f51aac3b03; _uetvid=3f6defe0237411ee9019e77acba71d73; __stripe_sid=73920c02-0bf4-411f-a64c-125d108ecacd1e068a; _clsk=15rn1py%7C1701374834607%7C2%7C0%7Cs.clarity.ms%2Fcollect; _dd_s=rum=0&expire=1701375862962; _gat=1; _ga=GA1.1.1683103711.1630637260; _ga_SZLSVQPSWG=GS1.1.1701374832.78.1.1701374963.59.0.0",
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