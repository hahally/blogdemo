from django.core.paginator import Paginator
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from reportlab.pdfgen import canvas

from blog.models import Post,Auth
from django.core.mail import send_mail

# Create your views here.

# 邮件发送
def sendEmail(subject,message,recipient_list):
    try:
        send_mail(
            subject = subject,                     # 标题
            message = message,                     # 正文
            recipient_list = recipient_list,       # 接收方
            from_email='2470607094@qq.com',      # 发送方
            auth_user = "2470607094@qq.com",     # 用于验证SMTP服务器的可选用户名
            auth_password = "wtbtimyrfezeeaci",  # 用于验证SMTP服务器的可选密码
            fail_silently=False,
        )
        print("success to send")
    except:
        print("fail to send")

# 首页访问次数
def visit(request):
    visits = request.session.get('visits', 1)
    request.session['visits'] = visits + 1
    # my_view(request)
    return visits

# 生成 PDF
def showPdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # buffer = io.BytesIO()
    p = canvas.Canvas(response)
    p.drawString(100, 100, "Hello world.")
    p.showPage()
    p.save()
    return response

# 首页视图
def index(request):
    posts = Post.objects.all()
    # 分页操作，4 篇一页，第一个参数为 object_list 对象
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context={
        'posts':posts,
        'visits':visit(request),
        'contacts':contacts,
    }
    return render(request, 'blog/index.html', context=context)

# 关于视图
def about(request):

    # auth = Auth.objects.get(name=name)
    #
    # print(auth)
    # context = {
    #     'auth':auth,
    # }

    return  render(request, 'blog/about.html')# ,context=context)

# 分类视图
def getTag(request,tag):
    post_list = Post.objects.filter(tag=tag)

    context = {'post_list':post_list,'tag':tag}
    return render(request, 'blog/tag_post_list.html', context)

# 文章列表视图
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    queryset = Post.objects.all()
    context_object_name = 'post_list'

# 文章详情视图
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'

from django.conf import settings
import os

# 上传文件视图

def upfile(request):

    return render(request, 'blog/upfile.html')


def savefile(request):

    if request.method == 'POST':
        file = request.FILES["file"]
        fpath = os.path.join(settings.MEDIA_ROOT,'user\ '+file.name)

        with open(fpath,'wb') as f:
            for info in file.chunks():
                f.write(info)
        f.close()
        return HttpResponse('<h1>上传成功</h1>')
    else:
        return HttpResponse('<h1>上传失败</h1>')


