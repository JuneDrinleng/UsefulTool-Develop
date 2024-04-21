import sys
from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import QApplication,QWidgetAction
from qframelesswindow import FramelessWindow
from Ui_update_try import Ui_Frame

class HelloWorld(FramelessWindow,Ui_Frame):
    def __init__(self):
        super(HelloWorld, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w=HelloWorld()
    w.show()
    app.exec_()