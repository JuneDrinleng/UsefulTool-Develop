import requests
import random
import json
from hashlib import md5
import os
import sys
import re
import html
from urllib import parse
import platform
import time
import hashlib
from PyDeepLX import PyDeepLX


# 百度翻译
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()
def Baidu_translator(input_text,from_lang,to_lang):
    system = platform.system()

    if system == 'Darwin':  # macOS
        cache_dir = os.path.expanduser('~/Library/Caches/Translate Helper/')
    elif system == 'Windows':
        cache_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'Translate Helper', 'Cache')
    else:
        raise ValueError(f'Unsupported operating system: {system}')

    # 确保缓存目录存在
    os.makedirs(cache_dir, exist_ok=True)

    # 定义缓存文件名和路径
    cache_file_path = os.path.join(cache_dir, 'settings_cache.json')
    with open(cache_file_path,'r') as f:
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
    try:
        result = r.json()['trans_result'][0]['dst']
        return result
    except KeyError as e:
            return f"错误原因：{e} \n 出错密码不准确活或填写账户密码，请检查api账户和密码"



# 谷歌翻译
def Google_translator(text, to_language, text_language):
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

def advanced_test_url(url):
    try:
        response = requests.get(url, timeout=3)  # 设置请求超时时间为5秒
        response.raise_for_status()  # 如果状态码不是200，将抛出HTTPError异常
        return '1'
    except:
        return '0'
    
def youdao_translator(content,to_language,text_language):
    salt = str(round(time.time() * 1000)) + str(random.randint(0, 9))
    data = "fanyideskweb" + content + salt + "Tbh5E8=q6U3EXe+&L[4c@"
    sign = hashlib.md5()
    sign.update(data.encode("utf-8"))
    sign = sign.hexdigest()

    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    headers = {
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-1927650476@223.97.13.65;',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
    }
    data = {
        'i': str(content),
        'from': text_language,
        'to': to_language,
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': str(salt),
        'sign': str(sign),
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }

    res = requests.post(url=url, headers=headers, data=data).json()
    return res['translateResult'][0][0]['tgt']

def deepL_translator(content,to_language,text_language):
    result=PyDeepLX.translate(content, text_language, to_language)
    return result
