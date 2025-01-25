from django.urls import path
from . import views  # 导入当前应用的视图

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]