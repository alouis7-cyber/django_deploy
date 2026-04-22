from django.urls import include, path
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("", lambda request: HttpResponse("Your Django app is running!")),

]
