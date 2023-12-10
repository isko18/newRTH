from django.urls import path
from apps.blog.views import *

urlpatterns = [
    path('', blog, name="blog"),
]