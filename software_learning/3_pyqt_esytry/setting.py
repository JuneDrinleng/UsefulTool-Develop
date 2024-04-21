import sys
from PyQt5.QtCore import Qt, QRect, QUrl,QLocale,QEvent
from PyQt5.QtGui import QIcon, QPainter, QImage, QBrush, QColor, QFont, QDesktopServices,QFontDatabase
from PyQt5.QtWidgets import QApplication, QFrame, QStackedWidget, QHBoxLayout, QLabel,QWidget,QLineEdit,QVBoxLayout,QAction,QTextBrowser,QGroupBox,QPlainTextEdit

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, NavigationWidget, MessageBox,
                            isDarkTheme, setTheme, Theme, setThemeColor, qrouter, FluentWindow, NavigationAvatarWidget)
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import PlainTextEdit,SearchLineEdit
from qframelesswindow import FramelessWindow, StandardTitleBar
from PyQt5.QtCore import pyqtSlot
from mymodel import *
from qfluentwidgets import CaptionLabel, PasswordLineEdit, SubtitleLabel, SwitchButton
import platform


class Widget(QFrame):

    def __init__(self, text: str,parent=None):
        super().__init__(parent=parent)
        self.label = QLabel(text, self)
        self.label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.label, 1,(Qt.AlignTop | Qt.AlignLeft) )
        self.setObjectName(text.replace(' ', '-'))
        self.label.installEventFilter(self)
        self.window_height_now=parent.window_height
        self.window_width_now=parent.window_width

    def eventFilter(self, obj, event):
        if obj == self.label and event.type() == QEvent.Resize:
            self.update_margins()
        return super().eventFilter(obj, event)

    def update_margins(self):
        # Calculate 10% of the width and height
        left_margin = int(self.window_width_now * 0.05)
        top_margin = int(self.window_height_now * 0.03)

        # Set the contents margins
        self.label.setContentsMargins(left_margin, top_margin, 0, 0)

class SettingWindow(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.user=None
        self.key=None
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
        self.PasswordLineEdit = PasswordLineEdit(self)
        self.PasswordLineEdit.setGeometry(QtCore.QRect(180, 260, 158, 33))
        self.PasswordLineEdit.setObjectName("PasswordLineEdit")
        self.PasswordLineEdit_2 = LineEdit(self)
        self.PasswordLineEdit_2.setGeometry(QtCore.QRect(180, 200, 158, 33))
        self.PasswordLineEdit_2.setObjectName("PasswordLineEdit_2")


        self.setStyleSheet("""
                QFrame {
                    background-color: rgb(249, 249, 249);
                }
            """)


        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setObjectName("setting")


        self.SwitchButton.checkedChanged.connect(self.toggle_main_window_stay_on_top)
        self.PasswordLineEdit.textChanged.connect(self.on_password_return_pressed)  # 添加returnPressed信号连接器
        self.PasswordLineEdit_2.textChanged.connect(self.on_password_return_pressed2)
    def on_password_return_pressed(self):  # 定义处理returnPressed信号的方法
            self.key = self.PasswordLineEdit.text()  # 获取并保存PasswordLineEdit中的文本至user变量   
            self.save_to_cache() 
    def on_password_return_pressed2(self):  # 定义处理returnPressed信号的方法
            self.user = self.PasswordLineEdit_2.text() # 获取并保存PasswordLineEdit中的文本至user变量  


    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.CaptionLabel.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:16pt;font-family: 华文中宋,Microsoft YaHei, 微软雅黑,PingFang SC, sans-serif;\">👀设置</span></p></body></html>"))
        self.SubtitleLabel.setText(_translate("Frame","<html><head/><body><p><font face='华文中宋,Microsoft YaHei, 微软雅黑,PingFang SC, sans-serif'>窗口锁定</font></p></body></html>"))
        self.SubtitleLabel_2.setText(_translate("Frame", "<html><head/><body><p><font face='华文中宋,Microsoft YaHei, 微软雅黑,PingFang SC, sans-serif'>API账户</font></p></body></html>"))
        self.SubtitleLabel_3.setText(_translate("Frame", "<html><head/><body><p><font face='华文中宋,Microsoft YaHei, 微软雅黑,PingFang SC, sans-serif'>API密钥</font></p></body></html>"))

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

        user_data={
             'appid':self.user,
             'appkey':self.key
        }

        with open(cache_file_path, 'w', encoding='utf-8') as file:
            json.dump(user_data, file, ensure_ascii=False, indent=4)
