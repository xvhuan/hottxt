import requests
import json

hotUrl = 'https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/86.0.4240.198 Safari/537.36'}
allResponse = requests.get(hotUrl, headers=headers).text
jsonDecode = json.loads(allResponse)
for i in range(15):
    print(str(i + 1) + '.' + jsonDecode["data"][i]["target"]["title"] + ' https://www.zhihu.com/question/' + str(
        jsonDecode["data"][i]["target"]["id"]))
