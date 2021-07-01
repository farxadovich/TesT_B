from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Category, Question, Choice


def index(request):
    category = Category.objects.all()
    return render(request, 'myapp/index.html', {'category': category})


def test(request, category):
    categ1 = Category.objects.get(pk=category)
    questions = Question.objects.filter(category=categ1)
    return render(request, 'myapp/test.html', {'questions': questions})


def check(request):
    print(request.GET)
    result = ''
    for key, value in request.GET.items():
        choice = Choice.objects.get(pk=value)
        print(choice)
        result = result + f"For Question {key},answer is {choice.correct}<br>"
    return HttpResponse(result)
