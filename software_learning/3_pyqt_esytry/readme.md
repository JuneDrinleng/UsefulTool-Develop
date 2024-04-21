打包命令：
~~~
pyinstaller -w --add-data "./resource/*:." -i "./resource/icon/logo.ico" -n "Translate Helper" --onefile main.py       
~~~
需要注意的是，打包时程序内的资源路径都得是绝对路径，否则会出错
程序最终的名字应该是Translate Helper