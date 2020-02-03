"""blogdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

class sitemaps():
    pass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),    # 路由配置
    path(r'mdeditor/', include('mdeditor.urls'))    # 提供编辑器本地上传的功能
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 用户上传的静态文件管理，生成环境不安全