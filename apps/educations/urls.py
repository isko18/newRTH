from django.urls import path
from apps.educations import views

urlpatterns = [
    path('', views.education, name="education"),
    path('cours/<int:pk>/', views.detail_courses, name='cours_detail'),
    path('intro/<int:pk>/', views.introduction_course, name='cours_intro'),
    path('opros/<int:pk>/', views.opros_course, name='cours_opros'),
    path('worksheet/<int:pk>/', views.worksheet_course, name='worksheet'),
    path('gender/<int:pk>/', views.gender, name='gender'),
    path('gender_discrimination/<int:pk>/', views.gender_discrimination, name='discrimination'),
    path('gender_norms/<int:pk>/', views.gender_norms, name='gender_norms'),
    path('gender_norms_stereotypes/<int:pk>/', views.gender_norms_stereotypes, name='gender_norms_stereotypes'),
    path('gender_norms_quality/<int:pk>/', views.gender_quality, name='gender_norm_quality'),
    path('laws/<int:pk>/', views.law, name='laws'),
    path('statistics/<int:pk>/', views.statistics, name='statistics'),
    path('education_video/<int:pk>/', views.education_video, name='video'),
    path('test_course/<int:pk>/', views.tests_course, name='test_course'),
    path('data/<str:data>/', views.get_data_of_user, name='data'),
]
