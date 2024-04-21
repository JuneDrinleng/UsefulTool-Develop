from setuptools import setup

APP = ['main.py']
DATA_FILES = [('.', ['config.json'])]
OPTIONS = {
    'iconfile': 'icon/icon_blue.icns',  # 替换为您的应用图标路径
    'argv_emulation': True,  # 允许命令行参数传递给应用
    'packages': ['model'],  # 包含 model.py 所在的模块
    'plist': {
           'CFBundleName': 'translator',
           'CFBundleDisplayName': 'Translation Helper',
           'CFBundleVersion': '1.0',
           'CFBundleShortVersionString': '1.0',
           'NSHumanReadableCopyright': 'Copyright © 2024 Sakura June',
       }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)