from setting import *
from translation import *

from PyQt5.QtWidgets import QApplication,QStackedWidget
from qframelesswindow import FramelessWindow, StandardTitleBar
from qfluentwidgets import (NavigationInterface, NavigationItemPosition)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,  QStackedWidget, QHBoxLayout


class MainWindow(FramelessWindow):

    def __init__(self):
        super().__init__()
        self.setTitleBar(StandardTitleBar(self))

        self.window_height=500
        self.window_width=400
        self.setFixedSize(self.window_width,self.window_height)
        self.hBoxLayout = QHBoxLayout(self)
        self.navigationInterface = NavigationInterface(self, showMenuButton=True)
        self.stackWidget = QStackedWidget(self)

        # create sub interface
        # self.translateInterfaceTiTle = Widget('🔠翻译', self)
        self.translateInterface = TranslationWindow(parent=self)
        self.settingInterface = SettingWindow(parent=self)
        self.settingInterface.set_main_window(self)
        # initialize layout
        self.initLayout()

        # add items to navigation interface
        self.initNavigation()

        self.initWindow()
    def toggle_always_on_top(self, state):
        # self.hide()
        if state:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
        # self.showNormal() # Update window appearance
        self.show() # 刷新窗口显示

    def initLayout(self):
        # 初始化窗口的布局，将导航界面和堆栈窗口部件添加到水平布局中。
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, self.titleBar.height(), 0, 0)
        self.hBoxLayout.addWidget(self.navigationInterface)
        self.hBoxLayout.addWidget(self.stackWidget)
        self.hBoxLayout.setStretchFactor(self.stackWidget, 1)

    def initNavigation(self):
        # 始化导航界面，添加子界面到导航界面和堆栈窗口部件中
        # enable acrylic effect
        self.navigationInterface.setAcrylicEnabled(True)
        file_path='D:\\GitHubStorage\\UsefulTool-Develop\\Translation\\5_restruct_translation'
        resource_path=os.path.join(file_path, 'resource')
        icon_path=os.path.join(resource_path, 'icon')

        tran_ico=os.path.join(icon_path, 'translation.svg')
        self.addSubInterface(self.translateInterface, tran_ico, '翻译')#这个是将子界面添加到导航栏
        self.navigationInterface.addSeparator()

        setting_ico=os.path.join(icon_path, 'setting.svg')
        self.addSubInterface(self.settingInterface, setting_ico, '设置', NavigationItemPosition.BOTTOM)



        self.stackWidget.currentChanged.connect(self.onCurrentInterfaceChanged)
        self.stackWidget.setCurrentIndex(1)


    def initWindow(self):
        # 设置窗口的大小、标题、图标等属性，并将窗口移动到屏幕中心
        self.resize(self.window_width, self.window_height)
        resource_path='D:\\GitHubStorage\\UsefulTool-Develop\\Translation\\5_restruct_translation\\resource'
        logo_path=os.path.join(resource_path, 'logo.ico')
        self.setWindowIcon(QIcon(logo_path))
        self.setWindowTitle('Translation Helper')
        self.titleBar.setAttribute(Qt.WA_StyledBackground)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)



        self.setQss()

    def addSubInterface(self, interface, icon, text: str, position=NavigationItemPosition.TOP, parent=None):
        """ add sub interface """
        #添加一个子界面到堆栈窗口部件和导航界面中
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
        #设置窗口的样式表
        file_path='D:\\GitHubStorage\\UsefulTool-Develop\\Translation\\5_restruct_translation'
        resource_path=os.path.join(file_path, 'resource')
        demo_path =os.path.join(os.path.join(resource_path, 'qss'),'demo.qss')
        with open(demo_path, encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def switchTo(self, widget):
        #切换到指定的子界面的方法
        self.stackWidget.setCurrentWidget(widget)

    def onCurrentInterfaceChanged(self, index):
        #堆栈窗口部件当前子界面改变时的槽函数，它会更新导航界面的当前项。
        widget = self.stackWidget.widget(index)
        self.navigationInterface.setCurrentItem(widget.objectName())