from model import *
from PyQt5.QtCore import Qt


# file_path='D:\\GitHubStorage\\UsefulTool-Develop\\Translation\\5_restruct_translation'
file_path=os.path.dirname(os.path.abspath(__file__))
def main():
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
    if not os.path.exists(cache_file_path):
        config_data={
            'appid':None,
            'appkey':None,
            'supplier':'谷歌翻译'
        }
        with open(cache_file_path, 'w', encoding='utf-8') as file:
            json.dump(config_data, file, ensure_ascii=False, indent=4)
    w=MainWindow(file_path=file_path)
    w.show()

if __name__ == '__main__':
    #设置清晰度问题
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    main()
    app.exec()
