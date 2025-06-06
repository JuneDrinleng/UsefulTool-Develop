import time
import threading
import os

import requests
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import webbrowser
from LogUtils import log, show_log

def open_browser(icon, item):
    port = 8080
    webbrowser.open(f"http://localhost:{port}")






def hot_search(url):
    
    response = requests.get(url)
    if response.status_code != 200:
        return None
    results = response.json()['data']
    realtime_hot = results['realtime']
    realtime_hot_df = pd.DataFrame(realtime_hot)['word']
    realtime_hot_str=realtime_hot_df.to_string(index=False)
    realtime_hot_top = (realtime_hot_str.splitlines()[0]).split(' ')[-1]
    return realtime_hot_str,realtime_hot_top



def create_emoji_icon(emoji_char="📟"):
    # 创建 64x64 图像
    img = Image.new('RGBA', (64, 64), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("seguiemj.ttf", 48)  # Windows emoji 字体
    except:
        font = ImageFont.load_default()

    # 用 textbbox 替代 textsize
    bbox = draw.textbbox((0, 0), emoji_char, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((64 - w) / 2, (64 - h) / 2), emoji_char, font=font, fill="black")

    return img

def on_quit(icon, item):
    icon.stop()
    os._exit(0)

def main():
    threading.Thread(target=keep_alive_loop, args=(TARGET_URL,), daemon=True).start()

    menu = Menu(
        MenuItem('查看日志', lambda icon, item: show_log()),
         MenuItem('打开浏览器', open_browser),
        MenuItem('退出', on_quit)
    )

    icon = Icon("KeepAlive", icon=create_emoji_icon("📟"), menu=menu)
    icon.run()

def keep_alive_loop(TARGET_URL):
    while True:
        try:
            realtime_hot_str,realtime_hot_top = hot_search(TARGET_URL)
            realtime_hot_str=realtime_hot_str.replace(" ","")
            log(f"实时热搜榜首: {realtime_hot_top}")
            time.sleep(INTERVAL_SECONDS)
        except Exception as e:
            log(f"Error: {e}")
            time.sleep(INTERVAL_SECONDS)
    


if __name__ == "__main__":
    log("Started with 📟 emoji tray icon")
    TARGET_URL = 'https://weibo.com/ajax/side/hotSearch'
    INTERVAL_SECONDS = 60
    main()
