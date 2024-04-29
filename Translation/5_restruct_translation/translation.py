from PyQt5.QtCore import QEvent,Qt,pyqtSignal
from PyQt5.QtWidgets import QFrame, QLabel,QVBoxLayout,QTextBrowser,QGroupBox
from mymodel import *
from qfluentwidgets import PlainTextEdit,TextEdit,ComboBox
import platform
from PyQt5 import QtCore

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

        self.comboBox=ComboBox(input_group_box)
        Translation_service_suppliers=['自动识别','英语','汉语']
        self.comboBox.setGeometry(220, 23, 100, 30)
        self.comboBox.addItems(Translation_service_suppliers)
        self.comboBox.setObjectName("comboBox_language")

        self.comboBox2=ComboBox(output_group_box)
        Translation_service_suppliers=['英语','汉语']
        self.comboBox2.setGeometry(220, 154, 100, 30)
        self.comboBox2.addItems(Translation_service_suppliers)
        self.comboBox2.setObjectName("comboBox_language_output")


        main_layout.addWidget(output_group_box)
        file_path='D:\\GitHubStorage\\UsefulTool-Develop\\Translation\\5_restruct_translation'
        resource_path=os.path.join(file_path, 'resource')
        transqss_path=os.path.join(os.path.join(resource_path, 'qss'),'translation.qss')
        with open(transqss_path, encoding='utf-8') as f:
            self.setStyleSheet(f.read())

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
            self.translate_sever=config_info['supplier']

        self.setLayout(main_layout)
        self.comboBox.currentTextChanged.connect(self.get_text_language)
        self.comboBox2.currentTextChanged.connect(self.get_target_language)
        self.text_language='auto'
        self.target_language='en'
    def get_text_language(self):
        self.text_language=self.comboBox.currentText()
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
            self.translate_sever=config_info['supplier']
        if self.text_language=='自动识别':
            self.text_language='auto'
        elif self.text_language=='英语':
            self.text_language='en'
        elif self.text_language=='汉语' and self.translate_sever=='谷歌翻译':
            self.text_language='zh-CN'
        elif self.text_language=='汉语' and self.translate_sever=='百度翻译':
            self.text_language='zh'
        elif self.text_language=='汉语' and self.translate_sever=='有道翻译':
            self.text_language='zh-CHS'
    def get_target_language(self):
        self.target_language=self.comboBox2.currentText()
        if self.target_language=='英语':
            self.target_language='en'
        elif self.target_language=='汉语' and self.translate_sever=='谷歌翻译':
            self.target_language='zh-CN'
        elif self.target_language=='汉语' and self.translate_sever=='百度翻译':
            self.target_language='zh'
        elif self.text_language=='汉语' and self.translate_sever=='有道翻译':
            self.text_language='zh-CHS'
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
            self.translate_sever=config_info['supplier']
        if self.translate_sever=='谷歌翻译':
            result=advanced_test_url('https://www.google.com')
            if result =='0':
                self.output_text_browser.setText('无法访问谷歌，请更换翻译服务提供商')
            else:
                if text==' ':
                    self.output_text_browser.setText('')
                else:
                    # self.output_text_browser.setText(Google_translator(text=text,text_language='zh-CN'))
                    self.output_text_browser.setText('翻译中，请稍等')
                    self.output_text_browser.setText(Google_translator(text=text,text_language=self.text_language,to_language=self.target_language))
        elif self.translate_sever=='百度翻译':
            self.output_text_browser.setText(Baidu_translator(input_text=text,from_lang=self.text_language,to_lang=self.target_language))
        elif self.translate_sever=='有道翻译':
            self.output_text_browser.setText(youdao_translator(content=text,text_language=self.text_language,to_language=self.target_language))
        elif self.translate_sever=='deepl翻译':
            self.output_text_browser.setText('翻译中，请稍等')
            self.output_text_browser.setText(deepL_translator(content=text,text_language=self.text_language,to_language=self.target_language))
            time.sleep(5)
class myPlainTextEdit(PlainTextEdit):
    enter_pressed = pyqtSignal(str)
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            text=self.toPlainText()
            self.enter_pressed.emit(text)  # 发射信号，携带当前文本内容
        else:
            super().keyPressEvent(event) 