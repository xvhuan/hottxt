import requests
import json
import urllib.parse

hotUrl = 'https://api.bilibili.com/x/web-interface/search/square?limit=10'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/86.0.4240.198 Safari/537.36'}
allResponse = requests.get(hotUrl, headers=headers).text
jsonDecode = json.loads(allResponse)["data"]["trending"]["list"]
for i in range(10):
    print(str(i + 1) + '.' + jsonDecode[i][
        "show_name"] + ' https://search.bilibili.com/all?keyword=' + urllib.parse.quote(jsonDecode[i]["keyword"]))
