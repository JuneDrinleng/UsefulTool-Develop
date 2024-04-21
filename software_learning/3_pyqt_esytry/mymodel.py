from typing import List, Union
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt, QRectF, pyqtSignal, QPoint, QTimer, QEvent, QAbstractItemModel, pyqtProperty
from qfluentwidgets import LineEdit,LineEditButton,PlainTextEdit
from qfluentwidgets import FluentIcon as FIF
import requests
import random
import json
from hashlib import md5
import os
import sys
import platform

# 用来使得搜索框按下回车可以搜索
class mySearchLineEdit(LineEdit):
    """ Search line edit """

    searchSignal = pyqtSignal(str)
    clearSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.searchButton = LineEditButton(FIF.SEARCH, self)

        self.hBoxLayout.addWidget(self.searchButton, 0, Qt.AlignRight)
        self.setClearButtonEnabled(True)
        self.setTextMargins(0, 0, 59, 0)

        self.searchButton.clicked.connect(self.search)
        self.clearButton.clicked.connect(self.clearSignal)
        self.returnPressed.connect(self.search)
    def search(self):
        """ emit search signal """
        text = self.text().strip()
        if text:
            self.searchSignal.emit(text)
        else:
            self.clearSignal.emit()

    def setClearButtonEnabled(self, enable: bool):
        self._isClearButtonEnabled = enable
        self.setTextMargins(0, 0, 28*enable+30, 0)

# 百度翻译
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()
def baidu_translator(input_text,from_lang='zh',to_lang='en'):
    # config_path=os.path.join(sys.argv[0],'..\\resource\\config.json')
    # config_path='D:\\GitHubStorage\\Course_and_Learning_resource\\software_learning\\3_pyqt_esytry\\resource\\config.json'
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
    config_path=cache_file_path
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
    try:
        result = r.json()['trans_result'][0]['dst']
        return result
    except KeyError as e:
            return f"错误原因：{e} \n 出错密码不准确活或填写账户密码，请检查api账户和密码"
    