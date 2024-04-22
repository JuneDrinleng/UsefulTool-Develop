# readme

## 1 操作细节

resoure文件夹绝对路径：

resource_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resource')

logo 绝对路径：
resource_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resource')
logo_path=os.path.join(resource_path, 'logo.ico')

谷歌翻译实现参考：https://www.perfcode.com/p/python-calls-google-translate-api.html

打包命令：
pyinstaller -w --add-data "./resource/*:." -i "./resource/logo.ico" -n "Translate Helper" --onefile main.py 



pyinstaller -w --add-data "./resource/*:." -i "./resource/logo.icns" -n "Translate Helper" --onefile main.py 

## 2 项目介绍

本项目利用PyQt-Fluent-Widgets提供的组件进行qt界面的实现，创造出了基于pyqt的GUI界面的翻译软件，已经在realise中发行打包的版本，项目实现功能如下：

- 程序窗口固定在屏幕最前端
- 百度翻译（需填写api）
- 谷歌翻译（类爬虫设计）
- 百度翻译和谷歌翻译的切换

程序的设置文件settings_cache.json位于此：

- Windows位于local app data 目录下的Translate Helper
- mac位于~/Library/Caches/Translate Helper/

