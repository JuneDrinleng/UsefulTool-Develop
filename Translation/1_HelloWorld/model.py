import tkinter as tk
import platform
# from tkinter import Entry
import json
from ttkbootstrap import Style, Entry, Label,Checkbutton

import requests
import random
import json
from hashlib import md5

def get_kai_font_name():
    system = platform.system()
    if system == 'Windows':
        return '楷体'
    elif system == 'Darwin':  # macOS
        return 'KaiTi'

class InputBox:
    def __init__(self, master):
        self.master = master

        self.entry_font = (get_kai_font_name(),10) #10控制输入框字号
        self.input_box = Entry(self.master,width=30, font=self.entry_font)
        self.input_box.place(x=20, y=40, anchor='nw')
        self.translation_label=None

    def get_text(self):
        return self.input_box.get()
    
    def handle_return(self,event):
        self.input_text=self.get_text()
        # translated_text=translator(self.input_text)
        translated_text=baidu_translator(self.input_text)
        self.display_translation(translated_text)

    def display_translation(self, translated_text):
        if self.translation_label is not None:
            # 如果label非空就销毁
            self.translation_label.destroy()
        text3 = translated_text
        front_style = ('Arial', 10)
        self.translation_label = Label(self.master, text=text3, font=front_style)
        self.translation_label.place(x=20, y=90, anchor='nw')  # 修改布局
    
    def bind_enter(self):
        self.input_box.bind('<Return>',self.handle_return)

def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()
def baidu_translator(input_text,from_lang='zh',to_lang='en'):

    with open('./config.json','r') as f:
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
    
#用于按钮
# def toggle_always_on_top(root):
#     current_state = root.winfo_toplevel().attributes("-topmost")
#     if current_state:
#         root.winfo_toplevel().attributes("-topmost", False)
#     else:
#         root.winfo_toplevel().attributes("-topmost", True)

def toggle_always_on_top(root, checkbutton):
    current_state = root.winfo_toplevel().attributes("-topmost")
    new_state = not current_state
    root.winfo_toplevel().attributes("-topmost", new_state)
    Checkbutton.select() if new_state else checkbutton.deselect()