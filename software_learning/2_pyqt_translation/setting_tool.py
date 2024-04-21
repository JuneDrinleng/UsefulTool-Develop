
from qfluentwidgets import PlainTextEdit
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5.QtCore import Qt
import requests
import random
import json
from hashlib import md5
from qframelesswindow import FramelessWindow

def translate():
    textEdit = PlainTextEdit()
    textEdit.setPlainText(input("请输入内容:"))

    # 获取普通文本
    input_text=textEdit.toPlainText()
    if input_text=="":
        print("请输入内容")
    else:
        translated_text=baidu_translator(input_text)
        print(translated_text)

def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()
def baidu_translator(input_text,from_lang='zh',to_lang='en'):
    try:
        with open('./config.json','r') as f:
            api_info=json.load(f)
            appid=api_info['appid']
            appkey=api_info['appkey']
    except Exception as e:
        print("请先配置api信息")

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

class MainWindow(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("翻译工具")
        self.setWindowIcon(self.windowIcon())
        self.setFixedSize(800, 600)
        

if __name__ == '__main__':
    #设置清晰度问题
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    MainWindow().show()
    app.exec()