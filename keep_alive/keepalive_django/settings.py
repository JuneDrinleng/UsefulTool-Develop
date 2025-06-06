import os
from pathlib import Path

# 项目根目录路径
BASE_DIR = Path(__file__).resolve().parent.parent

# 开发模式建议开启
DEBUG = True

# 允许访问的主机
ALLOWED_HOSTS = ["*"]

# 必须设置的密钥（开发环境随便设）
SECRET_KEY = "your-dev-secret-key"

# 安装的 Django 应用（含你写的 hotsearch）
INSTALLED_APPS = [
    'django.contrib.staticfiles',  # 静态文件支持
    'hotsearch',
]

MIDDLEWARE = []

ROOT_URLCONF = 'keepalive_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # 不需要额外指定，Django 会自动找 app 下的 templates/
        'APP_DIRS': True,
        'OPTIONS': {},
    },
]

WSGI_APPLICATION = 'keepalive_django.wsgi.application'

# 数据库可用 SQLite 暂时占位（你目前不使用）
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

# 本地语言和时间设置
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_TZ = False

# 静态文件（如 CSS/JS/图标）
STATIC_URL = '/static/'
