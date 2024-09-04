# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('resume/', views.generate_resume, name='generate_resume'),
]