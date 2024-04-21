resoure文件夹绝对路径：

resource_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resource')

logo 绝对路径：
resource_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resource')
logo_path=os.path.join(resource_path, 'logo.ico')

谷歌翻译实现参考：https://www.perfcode.com/p/python-calls-google-translate-api.html

打包命令：
pyinstaller -w --add-data "./resource/*:." -i "./resource/logo.ico" -n "Translate Helper" --onefile main.py 



pyinstaller -w --add-data "./resource/*:." -i "./resource/logo.icns" -n "Translate Helper" --onefile main.py 