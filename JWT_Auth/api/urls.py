from django.contrib import admin
from django.urls import path, include
from .views import StudentView

urlpatterns = [
    path("student", StudentView.as_view()),
]


