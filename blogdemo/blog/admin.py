from django.contrib import admin
from blog.models import Post,Auth
# Register your models here.

# 采用修饰符方式注册模型 与 admin.site.register(Post) 作用一样
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'auth','pub_date', 'tag', 'up_date')   # 显示字段
    list_filter = ('tag', 'pub_date')   # 侧栏的过滤器框
    fields = ('title','auth','desc','tag','pub_date','up_date','content')

@admin.register(Auth)
class AuthAdmin(admin.ModelAdmin):
    list_display = ('name','about')
    fields = ('name','about')