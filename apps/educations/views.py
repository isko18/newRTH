from __future__ import print_function
from django.shortcuts import render, get_object_or_404
from apps.educations import models
from apps.home.models import Harassment
from apps.home.models import Setting


# Create your views here.
def education(request):
    all_courses = models.Courses.objects.all()
    settings = Setting.objects.latest('id')
    harassment = Harassment.objects.latest('id')
    context = {
        'edus': all_courses, 
        'settings': settings,
        'harassment': harassment
    }
    return render(request, 'pages/education.html', context)


def detail_courses(request, pk):
    courses = get_object_or_404(models.Courses, pk=pk)
    return render(request, 'educations/index.html', {'courses': courses})


def introduction_course(request, pk):
    courses = get_object_or_404(models.Courses, pk=pk)
    intro = courses.course_intro.first()
    return render(request, 'educations/introduction.html', {'intro': intro, 'courses': courses})


def opros_course(request, pk):
    courses = get_object_or_404(models.Courses, pk=pk)
    opros = courses.course_servey.first()
    question = models.SurveyQuestion.objects.filter(survey=opros.id)
    return render(request, 'educations/opros.html',
                  {'opros': opros,
                   'courses': courses,
                   'question': question,
                   })


def worksheet_course(request, pk):
    courses = get_object_or_404(models.Courses, pk=pk)
    worksheet = courses.course_worksheet.first()
    return render(request, 'educations/worksheet.html', {'worksheet': worksheet, 'courses': courses})


def gender(request, pk):
    courses = get_object_or_404(models.Courses, pk=pk)
    genders = courses.course_gender.first()
    return render(request, 'educations/gender.html', {'genders': genders, 'courses': courses})


def gender_discrimination(request, pk):
    courses = get_object_or_404(models.Courses, pk=pk)
    discrimination = courses.course_gender_discrim.first()
    return render(request, 'educations/gender_discrimination.html', {'discrimination': discrimination,
                                                                     'courses': courses})


def gender_norms(request, pk):
    courses = get_object_or_404(models.Courses, pk=pk)
    gender_norm = courses.course_gender_norms.first()
    return render(request, 'educations/gender_norms.html', {'gender_norm': gender_norm, 'courses': courses})


def gender_norms_stereotypes(request, pk):
    courses = get_object_or_404(models.Courses, pk=pk)
    genders_stereotypes = courses.course_gender_norm.first()
    return render(request, 'educations/gender_norms_stereotypes.html', {'genders_stereotypes': genders_stereotypes,
                                                                        'courses': courses})


def gender_quality(request, pk):
    courses = get_object_or_404(models.Courses, pk=pk)
    genders_norm_quality = courses.course_gender_quality.first()
    return render(request, 'educations/gender_quality.html', {'genders_norm_quality': genders_norm_quality,
                                                              'courses': courses})


def law(request, pk):
    courses = get_object_or_404(models.Courses, pk=pk)
    laws = courses.course_laws.first()
    return render(request, 'educations/laws.html', {'laws': laws, 'courses': courses})


def statistics(request, pk):
    courses = get_object_or_404(models.Courses, pk=pk)
    course_image = get_object_or_404(models.StatisticImages, pk=pk)
    statistic = courses.course_statistics.first()
    return render(request, 'educations/statistics.html', {'statistic': statistic, 'courses': courses,
                                                          'course_image': course_image})


def education_video(request, pk):
    courses = get_object_or_404(models.Courses, pk=pk)
    video = courses.course_edus.first()
    return render(request, 'educations/video.html', {'video': video, 'courses': courses})


def tests_course(request, pk):
    courses = get_object_or_404(models.Courses, pk=pk)
    test = courses.course_test.first()
    print(test)
    anwers = models.TestQuestion.objects.filter(test=test.id)
    print(anwers)
    return render(request, 'educations/test.html',
                  {'test': test,
                   'question': anwers,
                   'courses': courses
                   })


def get_data_of_user(request, data):
    print(data)
    return render(request, 'educations/data.html', {'data': data})