import os
import sys
import urllib.request
import json
client_id = "v4KO7sTXQ_qLjAuX_ll4"
client_secret = "XG9X3gx_EK"
encText = urllib.parse.quote("They keep their songs about real life issues(depression, insomnia, etc.)﻿") # 따옴표 안에 번역할 내용 넣음.
data = "source=en&target=ko&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
    data = response_body.decode('utf-8')
    data = json.loads(data) # 딕셔너리화
    translated_text = data['message']['result']['translatedText']
    print("번역된 내용 : "+ translated_text)
else:
    print("Error Code:" + rescode)