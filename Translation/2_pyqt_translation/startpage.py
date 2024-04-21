# coding:utf-8
from qfluentwidgets import SplashScreen
from qframelesswindow import FramelessWindow, StandardTitleBar


class Demo(FramelessWindow):

    def __init__(self):
        super().__init__()
        self.resize(700, 600)
        self.setWindowTitle('PyQt-Fluent-Widgets')
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))

        # 1. 创建启动页面
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(102, 102))

        # 2. 在创建其他子页面前先显示主界面
        self.show()

        # 3. 创建子界面
        self.createSubInterface()

        # 4. 隐藏启动页面
        self.splashScreen.finish()

    def createSubInterface(self):
        loop = QEventLoop(self)
        QTimer.singleShot(3000, loop.quit)
        loop.exec()


