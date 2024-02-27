import os
import sys
import urllib.request

client_id = "bfn0c2j2ptXMT1dw_6fU"
client_secret = "FpPRsna1qp"

encText = urllib.parse.quote("충무로 점심")

title_lst = []
description_lst=[]

for pageNum in range(1, 1000, 100):
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
    suburl = '&display=100&start='
    url = url + suburl + str(pageNum)

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        items = json.loads(response_body.decode('utf-8'))['items']
        for item in items:
            title_lst.append(item['title'])
            description_lst.append(item['description'])
    else:
        print("Error Code:" + rescode)
        break

with open('충무로맛집블로그제목.txt', 'w', encoding='utf-8') as f:
    for tit in title_lst:
        f.write(tit + '\n')
with open('충무로맛집블로그본문.txt', 'w', encoding='utf-8') as f:
    for des in description_lst:
        f.write(des + '\n')












52