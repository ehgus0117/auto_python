import os
import sys
import urllib.request, json


client_id = "kG1xEc91YMteojwu8G9b" 
client_secret = "Rg_j9naH_t"

print("어서오세요. 파파고 API ko -> en 번역기 입니다.\n종료하려면 q를 입력해주세요")
trans = '번역할 한국어 입력: '

while 1:

    text = input()
    if text == 'q':
        break
    else:
        print(trans + text)
    encText = urllib.parse.quote(text)


    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        response_body = response_body.decode('utf-8')
        strToJson = json.loads(response_body)
        enText = strToJson['message']['result']['translatedText']
        print('번역 결과: ' + enText)
    else:
        print("Error Code:" + rescode)