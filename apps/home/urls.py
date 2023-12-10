from django.urls import path
from apps.home.views import index, join, donation

urlpatterns = [
    path('', index, name="home"),
    path('join', join, name="join"),
    path('donation', donation, name="donation"),
]