from django.shortcuts import render
from apps.home.models import Setting, AboutUs
from apps.projects.models import Projects


def index(request):
    settings = Setting.objects.latest('id')
    aboutus = AboutUs.objects.latest('id')
    projects = Projects.objects.latest('id')
    context = {
        'settings': settings,
        'aboutus': aboutus,
        'projects': projects,
    }
    return render(request, 'index.html', context)


def join(request):
    settings = Setting.objects.latest('id')
    context = {
        'settings': settings,
    }
    return render(request, 'pages/join.html', context)


def donation(request):
    settings = Setting.objects.latest('id')
    context = {
        'settings': settings,
    }
    return render(request, 'pages/donation.html', context)