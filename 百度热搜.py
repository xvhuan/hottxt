import requests
import re
import json

hotUrl = 'https://www.baidu.com/s?wd=%E8%99%9A%E5%B9%BBblog&rsv_spt=1&rsv_iqid=0x8424c7bd00024a91&issp=1&f=8&rsv_bp=1' \
         '&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_dl=ib&rsv_enter=0&rsv_sug3=11&rsv_sug1=10&rsv_sug7=100&rsv_btype=i' \
         '&inputT=8722&rsv_sug4=8722 '
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 '
                  'Safari/537.36'}
hotResponse = requests.get(hotUrl, headers=headers, cookies={"BAIDUID":"AD6E5512A1E4FE9169523EDFA51CB233"}).content.decode()
hotTxt = re.findall('pmd"><!--s-data:(.*)--', hotResponse)
allHotTxt = json.loads(hotTxt[0])["bdlistGroup"][0]
for i in range(15):
    hotTitle = allHotTxt[i]["link"]
    hotLeftUrl = allHotTxt[i]["leftUrl"]
    print(str(i+1) + '.' + hotTitle + ' https://www.baidu.com' + hotLeftUrl)
