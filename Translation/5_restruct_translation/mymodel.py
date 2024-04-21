import requests
import random
import json
from hashlib import md5
import os
import sys
import re
import html
from urllib import parse


# 百度翻译
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()
def Baidu_translator(input_text,from_lang='zh',to_lang='en'):
    config_path=os.path.join(sys.argv[0],'..//config.json')
    with open(config_path,'r') as f:
        api_info=json.load(f)
        appid=api_info['appid']
        appkey=api_info['appkey']


    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    query = input_text

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()['trans_result'][0]['dst']
    return result



# 谷歌翻译
def Google_translator(text, to_language="auto", text_language="auto"):
    GOOGLE_TRANSLATE_URL = 'http://translate.google.com/m?q=%s&tl=%s&sl=%s'
    text = parse.quote(text)
    url = GOOGLE_TRANSLATE_URL % (text,to_language,text_language)
    response = requests.get(url)
    data = response.text
    expr = r'(?s)class="(?:t0|result-container)">(.*?)<'
    result = re.findall(expr, data)
    if (len(result) == 0):
        return ""

    return html.unescape(result[0])

# print(Googletranslate("你吃饭了么?", "en","zh-CN")) #汉语转英语
# print(Googletranslate("你吃饭了么？", "ja","zh-CN")) #汉语转日语
# print(Googletranslate("about your situation", "zh-CN","en")) #英语转汉语