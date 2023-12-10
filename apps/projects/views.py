from django.shortcuts import render
from apps.home.models import Setting
from apps.projects.models import Projects, InisiativMiniProjects, Gallery, Partners
from django.views.generic.base import View


# Create your views here.
def projects(request):
    settings = Setting.objects.get(pk=1)
    projects_last = Projects.objects.latest('id')
    projects_menu = Projects.objects.all()
    inisiativMiniprojects_menu = InisiativMiniProjects.objects.all()
    context = {
        'settings': settings,
        'projects_last': projects_last,
        'projects_menu': projects_menu,
        'inisiativMiniprojects_menu': inisiativMiniprojects_menu,
    }
    return render(request, 'pages/projects.html', context)


class ProjectsDetailView(View):
    def get(self, request, slug):
        settings = Setting.objects.get(pk=1)
        projects_last = Projects.objects.latest('id')
        projects_menus = Projects.objects.all()
        projects = Projects.objects.get(slug=slug)
        inisiativMiniprojects_menu = InisiativMiniProjects.objects.all()
        context = {
            'settings': settings,
            'projects': projects,
            'projects_last': projects_last,
            'projects_menus': projects_menus,
            'inisiativMiniprojects_menu': inisiativMiniprojects_menu,
        }
        return render(request, "page_detail/projects_detail.html", context)


class InisiativMiniProjectsDetailView(View):
    def get(self, request, slug):
        settings = Setting.objects.get(pk=1)
        projects_menus = Projects.objects.all()
        insminiproj = InisiativMiniProjects.objects.get(slug=slug)
        inisiativMiniprojects_menu = InisiativMiniProjects.objects.all()
        context = {
            'settings': settings,
            'insminiproj': insminiproj,
            'projects_menus': projects_menus,
            'inisiativMiniprojects_menu': inisiativMiniprojects_menu,
        }
        return render(request, "page_detail/inis_mini_proj.html", context)


def gallery(request):
    settings = Setting.objects.latest('id')
    gallery = Gallery.objects.all()
    context = {
        'settings': settings,
        'gallery': gallery,
    }
    return render(request, 'pages/gallery.html', context)


def partners(request):
    settings = Setting.objects.get(pk=1)
    partners = Partners.objects.all()
    context = {
        'settings': settings,
        'partners': partners,
    }
    return render(request, 'pages/partners.html', context)


class PartnersDetailView(View):
    def get(self, request, slug):
        settings = Setting.objects.get(pk=1)
        partners = Partners.objects.get(slug=slug)
        context = {
            'settings': settings,
            'partners': partners,
        }
        return render(request, "page_detail/partner_detail.html", context)