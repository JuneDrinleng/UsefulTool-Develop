# coding:utf-8
import sys
from PyQt5.QtCore import Qt, QRect, QUrl,QLocale,QEvent
from PyQt5.QtGui import QIcon, QPainter, QImage, QBrush, QColor, QFont, QDesktopServices,QFontDatabase
from PyQt5.QtWidgets import QApplication, QFrame, QStackedWidget, QHBoxLayout, QLabel,QWidget,QLineEdit,QVBoxLayout,QAction

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, NavigationWidget, MessageBox,
                            isDarkTheme, setTheme, Theme, setThemeColor, qrouter, FluentWindow, NavigationAvatarWidget)
from qfluentwidgets import FluentIcon as FIF
from qframelesswindow import FramelessWindow, StandardTitleBar


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        # 加载自定义字体
        # font_id = QFontDatabase.addApplicationFont('Font/huawenzhongsong.ttf')
        # font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        # font = QFont(font_family, 12, QFont.Bold)
        self.label = QLabel(text, self)
        # self.label.setFont(font)
        # self.label.setAlignment(Qt.AlignCenter)
        self.label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.hBoxLayout = QHBoxLayout(self)
        # self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignTop | Qt.AlignLeft)
        self.setObjectName(text.replace(' ', '-'))

        # Connect resizeEvent signal to update_margins slot
        self.label.installEventFilter(self)
    def eventFilter(self, obj, event):
        if obj == self.label and event.type() == QEvent.Resize:
            self.update_margins()
        return super().eventFilter(obj, event)

    def update_margins(self):
        width = self.label.width()
        height = self.label.height()

        # Calculate 10% of the width and height
        left_margin = int(width * 0.4)
        top_margin = int(height * 0.5)

        # Set the contents margins
        self.label.setContentsMargins(left_margin, top_margin, 0, 0)


class MainWindow(FramelessWindow):

    def __init__(self):
        super().__init__()
        self.setTitleBar(StandardTitleBar(self))

        # use dark theme mode
        # setTheme(Theme.DARK)

        # change the theme color
        # setThemeColor('#0078d4')

        self.hBoxLayout = QHBoxLayout(self)
        self.navigationInterface = NavigationInterface(self, showMenuButton=True)
        self.stackWidget = QStackedWidget(self)

        # create sub interface
        self.translateInterface = Widget('翻译 🔠', self)
        
        self.settingInterface = Widget('设置 ⚙ ', self)

        # initialize layout
        self.initLayout()

        # add items to navigation interface
        self.initNavigation()

        self.initWindow()

    def initLayout(self):
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, self.titleBar.height(), 0, 0)
        self.hBoxLayout.addWidget(self.navigationInterface)
        self.hBoxLayout.addWidget(self.stackWidget)
        self.hBoxLayout.setStretchFactor(self.stackWidget, 1)

    def initNavigation(self):
        # enable acrylic effect
        self.navigationInterface.setAcrylicEnabled(True)

        self.addSubInterface(self.translateInterface, 'icon/translation.svg', '翻译')

        self.navigationInterface.addSeparator()

        # add custom widget to bottom
        # self.navigationInterface.addWidget(
        #     routeKey='avatar',
        #     widget=NavigationAvatarWidget('zhiyiYo', 'resource/shoko.png'),
        #     onClick=self.showMessageBox,
        #     position=NavigationItemPosition.BOTTOM,
        # )

        self.addSubInterface(self.settingInterface, 'icon/setting.svg', '设置', NavigationItemPosition.BOTTOM)



        self.stackWidget.currentChanged.connect(self.onCurrentInterfaceChanged)
        self.stackWidget.setCurrentIndex(1)


    def initWindow(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon('icon/logo.svg'))
        self.setWindowTitle('Translation Helper')
        self.titleBar.setAttribute(Qt.WA_StyledBackground)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

        # NOTE: set the minimum window width that allows the navigation panel to be expanded
        # self.navigationInterface.setMinimumExpandWidth(900)
        # self.navigationInterface.expand(useAni=False)

        self.setQss()

    def addSubInterface(self, interface, icon, text: str, position=NavigationItemPosition.TOP, parent=None):
        """ add sub interface """
        self.stackWidget.addWidget(interface)
        self.navigationInterface.addItem(
            routeKey=interface.objectName(),
            icon=icon,
            text=text,
            onClick=lambda: self.switchTo(interface),
            position=position,
            tooltip=text,
            parentRouteKey=parent.objectName() if parent else None
        )

    def setQss(self):
        color = 'dark' if isDarkTheme() else 'light'
        with open(f'resource/{color}/demo.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def switchTo(self, widget):
        self.stackWidget.setCurrentWidget(widget)

    def onCurrentInterfaceChanged(self, index):
        widget = self.stackWidget.widget(index)
        self.navigationInterface.setCurrentItem(widget.objectName())

        #!IMPORTANT: This line of code needs to be uncommented if the return button is enabled
        # qrouter.push(self.stackWidget, widget.objectName())

    def showMessageBox(self):
        w = MessageBox(
            '支持作者🥰',
            '个人开发不易，如果这个项目帮助到了您，可以考虑请作者喝一瓶快乐水🥤。您的支持就是作者开发和维护项目的动力🚀',
            self
        )
        w.yesButton.setText('来啦老弟')
        w.cancelButton.setText('下次一定')

        if w.exec():
            QDesktopServices.openUrl(QUrl("https://afdian.net/a/zhiyiYo"))


