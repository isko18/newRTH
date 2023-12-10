from django.shortcuts import render
from apps.home.models import Setting
from apps.blog.models import News

# Create your views here.
def blog(request):
    settings = Setting.objects.get(pk=1)
    news = News.objects.all()
    context = {
        'settings': settings,
        "news":news,
    }
    return render(request, 'pages/blog.html', context)