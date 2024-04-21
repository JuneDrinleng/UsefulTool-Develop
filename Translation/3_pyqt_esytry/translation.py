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

class TranslationWindow(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window_height=parent.window_height
        self.window_width=parent.window_width
        # 主布局管理器
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # 标题标签
        self.label_title = QLabel("▶ 🔠 翻译 ", self)
        main_layout.addWidget(self.label_title)
        self.label_title.installEventFilter(self)

        # 输入部分 QGroupBox
        input_group_box = QGroupBox("需要翻译的文本：")
        input_layout = QVBoxLayout(input_group_box)
        input_layout.setContentsMargins(20, 10, 10, 10)  #调节输入框的位置
        input_layout.setSpacing(10)

        # # 输入提示标签
        # self.label_input = QLabel("需要翻译的文本：", input_group_box)
        # input_layout.addWidget(self.label_input)

        # 输入框
        # self.input_line_edit = QLineEdit(input_group_box)
        # input_layout.addWidget(self.input_line_edit)
        self.input_line_edit=mySearchLineEdit(input_group_box)
        self.input_line_edit.searchSignal.connect(self.output_text)

        input_layout.addWidget(self.input_line_edit)

        main_layout.addWidget(input_group_box)

        # 输出部分 QGroupBox
        output_group_box = QGroupBox("翻译结果")
        output_layout = QVBoxLayout(output_group_box)
        output_layout.setContentsMargins(10, 10, 10, 10)
        output_layout.setSpacing(10)

        # 输出提示标签
        # self.label_output = QLabel("翻译结果：", output_group_box)
        # output_layout.addWidget(self.label_output)

        # 结果框
        self.output_text_browser = QTextBrowser(output_group_box)
        output_layout.addWidget(self.output_text_browser)

        main_layout.addWidget(output_group_box)
        # transqss_path=os.path.join(sys.argv[0],'..\\resource\\style_format\\translation.qss')
        transqss_path='D:\\GitHubStorage\\Course_and_Learning_resource\\software_learning\\3_pyqt_esytry\\resource\\style_format\\translation.qss'
        with open(transqss_path, encoding='utf-8') as f:
            self.setStyleSheet(f.read())

        self.setLayout(main_layout)

    def eventFilter(self, obj, event):
        if obj == self.label_title and event.type() == QEvent.Resize:
            self.update_margins()
        return super().eventFilter(obj, event)

    def update_margins(self):
        width = self.label_title.width()
        height = self.label_title.height()

        # Calculate 10% of the width and height
        left_margin = int(self.window_width * 0.01)
        top_margin = int(self.window_height * 0.01)

        # Set the contents margins
        self.label_title.setContentsMargins(left_margin, top_margin, 0, 0)
    
    def output_text(self,text):
        self.output_text_browser.setText(baidu_translator(input_text=text))