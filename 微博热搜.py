import requests
import re

hotTxt = requests.get("https://s.weibo.com/top/summary").content.decode()
newHotTxt = hotTxt.replace('\n', '')
newHotTxt = newHotTxt.replace(" ", "")
noTdTxt = re.findall("<tbody>(.*?)</tbody>", newHotTxt)[0]
arrayTxt = re.findall('ranktop">(.*?)</a>', noTdTxt)
for x in range(15):
    ft = arrayTxt[x]
    # rank = arrayTxt[0:x.rfind("</")] #热搜排名
    urlTxt = ft.split('"') #热搜链接
    hotName = ft.split(">")  # 热搜名称
    hotTxtSave = str(x + 1) + "." + hotName[3] + ' https://s.weibo.com' + urlTxt[3]
    print(hotTxtSave)
