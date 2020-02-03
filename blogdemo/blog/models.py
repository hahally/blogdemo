from django.db import models
from django.urls import reverse
from mdeditor.fields import MDTextField   # markdown相关包
import markdown
# Create your models here.


class Post(models.Model):

    auth = models.ForeignKey('Auth', on_delete=models.CASCADE)

    title = models.CharField(verbose_name="标题",max_length=50)   # CharField 的 max_length 属性是必须的

    desc = models.CharField(verbose_name="简述",max_length=200,null=True,blank=True)

    pub_date = models.DateTimeField(verbose_name="发布日期")

    up_date = models.DateTimeField(verbose_name="更新日期",null=True,blank=True)

    content = MDTextField(verbose_name="内容")     # 集成文本编辑器

    tags = (("ME","杂记"),("TE","杂技"))

    tag = models.CharField(verbose_name="标签",choices=tags,max_length=10)

    visits = models.PositiveIntegerField(verbose_name="访问量",default=0)  # 访问量存储字段，初始值 0

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[str(self.id)])

    def get_tag_url(self):

        return reverse('blog:tag_post_list',args=[self.tag])

    def get_auth_url(self):

        return reverse('blog:about',args=[self.auth])

    def get_visits(self):
        self.visits = self.visits+1
        self.save(update_fields=['visits'])

        return self.visits

    def get_content_as_markdown(self):
        self.content = markdown.markdown(
        self.content,extensions = [
            # 包含 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
            # 自动生成目录
            'markdown.extensions.toc',
			]
		)
        return self.content #markdown.markdown(self.content, safe_mode='escape')

    def get_toc(self):
        md =  markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        ])
        self.content = md.convert(self.content)
        self.toc = md.toc
        if len(self.toc)==35:

            self.toc = ""
            return self.toc

        return "<h3>目录</h3>"+self.toc

    class Meta:
        ordering = ["-pub_date"]

class Auth(models.Model):

    name = models.CharField(verbose_name='名字',max_length=50)

    about = models.TextField(verbose_name='关于',null=True,blank=False,default="暂无介绍")

    def __str__(self):

        return self.name