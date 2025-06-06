import sys
import os
import time
def get_log_path():
    return os.path.join(os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__), "keepalive.log")

def log(msg):
    timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
    full_msg = f"{timestamp} {msg}"
    with open(get_log_path(), "a", encoding="utf-8") as f:
        f.write(full_msg + "\n")

def show_log():
    os.startfile(get_log_path())