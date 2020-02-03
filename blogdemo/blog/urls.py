from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.index,name='index'),     # 入口路由
    path('about/',views.about,name='about'), # about 视图
    path('post/<int:pk>',views.PostDetailView.as_view(),name='post_detail'), # 详情视图 使用DetailView 参数名必须取pk
    path('post/all/',views.PostListView.as_view(),name='post_list'),    # 文章列表
    path('post/tags/<str:tag>',views.getTag,name='tag_post_list'),       # 分类
    path('upfile/',views.upfile,name='upfile'),   # 上传文件
    path('savefile/',views.savefile,name='savefile'),   # 上传文件

    path('pdf/',views.showPdf,name='pdf'),
]