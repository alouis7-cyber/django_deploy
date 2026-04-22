from django.shortcuts import render
from .models import Question

def index(request):
    latest_questions = Question.objects.all()
    context = {"questions": latest_questions}
    return render(request, "polls/index.html", context)

