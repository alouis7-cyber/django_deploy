from django.urls import include, path
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("polls/", include("polls.urls")),
]
