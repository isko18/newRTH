from django.urls import path
from apps.projects.views import *

urlpatterns = [
    path('', projects, name="projects"),
    path('<str:slug>/', ProjectsDetailView.as_view(), name="projects_detail"),
    path('partners/<str:slug>/', PartnersDetailView.as_view(), name="partners_detail"),
    path('proj/<str:slug>/', InisiativMiniProjectsDetailView.as_view(), name="inisiativ_mini_projects_detail"),
    
]