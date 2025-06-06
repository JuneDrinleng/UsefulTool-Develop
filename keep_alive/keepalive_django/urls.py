from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('hotsearch.urls')),  # 把根路径交给 hotsearch 应用处理
]
