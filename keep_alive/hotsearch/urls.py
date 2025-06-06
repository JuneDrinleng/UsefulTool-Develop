from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 访问 / 时，调用 views.home
]
