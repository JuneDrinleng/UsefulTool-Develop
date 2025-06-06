import threading
import subprocess
import os
import time
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw, ImageFont
import webbrowser

# 创建 emoji 图标
def create_emoji_icon(emoji_char="📟"):
    img = Image.new('RGBA', (64, 64), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("seguiemj.ttf", 48)
    except:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), emoji_char, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((64 - w) / 2, (64 - h) / 2), emoji_char, font=font, fill="black")
    return img

# 打开网页
def open_browser(icon, item):
    webbrowser.open("http://localhost:8080")

# 启动 Django 服务器（后台运行）
def start_django_server():
    subprocess.Popen(["python", "manage.py", "runserver", "8080"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# 托盘退出
def on_quit(icon, item):
    icon.stop()
    os._exit(0)

# 托盘主函数
def run_tray():
    menu = Menu(
        MenuItem("打开浏览器", open_browser),
        MenuItem("退出", on_quit)
    )
    icon = Icon("KeepAlive", icon=create_emoji_icon("📟"), menu=menu)
    icon.run()

if __name__ == "__main__":
    threading.Thread(target=start_django_server, daemon=True).start()
    time.sleep(1)
    run_tray()
