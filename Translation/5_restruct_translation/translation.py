from PyQt5.QtCore import QEvent,Qt,pyqtSignal
from PyQt5.QtWidgets import QFrame, QLabel,QVBoxLayout,QTextBrowser,QGroupBox
from mymodel import *
from qfluentwidgets import PlainTextEdit,TextEdit
import platform

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
        
        self.input_line_edit=myPlainTextEdit(input_group_box)
        self.input_line_edit.enter_pressed.connect(self.output_text)
        # self.input_line_edit.keyPressEvent.connect(self.output_text)

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
        resource_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resource')
        transqss_path=os.path.join(os.path.join(resource_path, 'qss'),'translation.qss')
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
        with open(cache_file_path, 'r', encoding='utf-8') as file:
            config_info=json.load(file)
            translate_sever=config_info['supplier']
        if translate_sever=='谷歌翻译':
            if text==' ':
                self.output_text_browser.setText('')
            else:
                self.output_text_browser.setText(Google_translator(text=text,text_language='zh-CN'))
        elif translate_sever=='百度翻译':
            self.output_text_browser.setText(Baidu_translator(input_text=text))


class myPlainTextEdit(PlainTextEdit):
    enter_pressed = pyqtSignal(str)
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            text=self.toPlainText()
            self.enter_pressed.emit(text)  # 发射信号，携带当前文本内容
        else:
            super().keyPressEvent(event) 