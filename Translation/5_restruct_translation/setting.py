from PyQt5.QtWidgets import  QFrame
from mymodel import *
from qfluentwidgets import CaptionLabel, PasswordLineEdit, SubtitleLabel, SwitchButton,LineEdit,ComboBox
import platform
from PyQt5 import QtCore



class SettingWindow(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.user=None
        self.key=None
        self.translater_supplier="谷歌翻译"
        self.window_height=parent.window_height
        self.window_width=parent.window_width
        self.SwitchButton = SwitchButton(self)
        self.SwitchButton.setGeometry(QtCore.QRect(200, 130, 76, 22))
        self.SwitchButton.setObjectName("SwitchButton")
        self.CaptionLabel = CaptionLabel(self)
        self.CaptionLabel.setGeometry(QtCore.QRect(50, 40, 91, 41))
        self.CaptionLabel.setObjectName("CaptionLabel")
        self.SubtitleLabel = SubtitleLabel(self)
        self.SubtitleLabel.setGeometry(QtCore.QRect(50, 120, 120, 27))
        self.SubtitleLabel.setObjectName("SubtitleLabel")
        self.SubtitleLabel_2 = SubtitleLabel(self)
        self.SubtitleLabel_2.setGeometry(QtCore.QRect(50, 200, 120, 27))
        self.SubtitleLabel_2.setObjectName("SubtitleLabel_2")
        self.SubtitleLabel_3 = SubtitleLabel(self)
        self.SubtitleLabel_3.setGeometry(QtCore.QRect(50, 260, 120, 27))
        self.SubtitleLabel_3.setObjectName("SubtitleLabel_3")
        self.SubtitleLabel_4 = SubtitleLabel(self)
        self.SubtitleLabel_4.setGeometry(QtCore.QRect(50, 350, 120, 27))
        self.SubtitleLabel_4.setObjectName("SubtitleLabel_4")
        self.PasswordLineEdit = PasswordLineEdit(self)
        self.PasswordLineEdit.setGeometry(QtCore.QRect(180, 260, 158, 33))
        self.PasswordLineEdit.setObjectName("PasswordLineEdit")
        self.PasswordLineEdit_2 = LineEdit(self)
        self.PasswordLineEdit_2.setGeometry(QtCore.QRect(180, 200, 158, 33))
        self.PasswordLineEdit_2.setObjectName("PasswordLineEdit_2")
        self.comboBox=ComboBox(self)
        Translation_service_suppliers=['未选择','谷歌翻译','百度翻译','有道翻译','deepl翻译']
        self.comboBox.addItems(Translation_service_suppliers)
        self.comboBox.setGeometry(QtCore.QRect(180, 350, 158, 33))
        self.comboBox.setObjectName("comboBox")
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
        if os.path.exists(cache_file_path):  # 如果缓存文件存在，则读取缓存内容
            with open(cache_file_path, 'r', encoding='utf-8') as file:
                user_info=json.load(file)
                usal_supplier=user_info['supplier']
                self.user=user_info['appid']
                self.key=user_info['appkey']
            self.comboBox.setPlaceholderText(f"{usal_supplier}")
            self.PasswordLineEdit_2.setText(self.user)
            self.PasswordLineEdit.setText(self.key)
        else:  # 如果缓存文件不存在，则使用默认值
            self.comboBox.setPlaceholderText("谷歌翻译")

        self.setStyleSheet("""
                QFrame {
                    background-color: rgb(249, 249, 249);
                }
            """)


        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setObjectName("setting")


        #槽函数
        # self.comboBox.currentText().connect(self.save_translater_supplier)
        self.comboBox.currentIndexChanged.connect(self.save_translater_supplier)
        self.SwitchButton.checkedChanged.connect(self.toggle_main_window_stay_on_top)
        self.PasswordLineEdit.textChanged.connect(self.on_password_return_pressed)  # 添加returnPressed信号连接器
        self.PasswordLineEdit_2.textChanged.connect(self.on_password_return_pressed2)

    def save_translater_supplier(self):
        #保存翻译服务提供商
        self.translater_supplier=self.comboBox.currentText()
        self.save_to_cache()


    def on_password_return_pressed(self):  # 定义处理returnPressed信号的方法
            self.key = self.PasswordLineEdit.text()  # 获取并保存PasswordLineEdit中的文本至user变量   
            self.save_to_cache() 
    def on_password_return_pressed2(self):  # 定义处理returnPressed信号的方法
            self.user = self.PasswordLineEdit_2.text() # 获取并保存PasswordLineEdit中的文本至user变量  
            self.save_to_cache()


    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.CaptionLabel.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:16pt;font-family: 华文中宋,Microsoft YaHei, 微软雅黑,PingFang SC, sans-serif;\">👀设置</span></p></body></html>"))
        self.SubtitleLabel.setText(_translate("Frame","<html><head/><body><p><font face='华文中宋,Microsoft YaHei, 微软雅黑,PingFang SC, sans-serif'>窗口锁定</font></p></body></html>"))
        self.SubtitleLabel_2.setText(_translate("Frame", "<html><head/><body><p><font face='华文中宋,Microsoft YaHei, 微软雅黑,PingFang SC, sans-serif'>百度API账户</font></p></body></html>"))
        self.SubtitleLabel_3.setText(_translate("Frame", "<html><head/><body><p><font face='华文中宋,Microsoft YaHei, 微软雅黑,PingFang SC, sans-serif'>百度API密钥</font></p></body></html>"))
        self.SubtitleLabel_4.setText(_translate("Frame", "<html><head/><body><p><font face='华文中宋,Microsoft YaHei, 微软雅黑,PingFang SC, sans-serif'>翻译提供者</font></p></body></html>"))

    def set_main_window(self, main_window):
            self.main_window = main_window

    def toggle_main_window_stay_on_top(self, state):
        self.main_window.toggle_always_on_top(state)

    def save_to_cache(self):
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
        config_data={
            'appid':self.user,
            'appkey':self.key,
            'supplier':self.translater_supplier
        }
        with open(cache_file_path, 'w', encoding='utf-8') as file:
            json.dump(config_data, file, ensure_ascii=False, indent=4)