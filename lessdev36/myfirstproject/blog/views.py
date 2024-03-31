from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Главная</h1>')

def about(request):
    return HttpResponse('<h1>Вторая страница</h1>')


def greet(request, name):
    return HttpResponse(f"Привет, {name}!")


def index(request):
    return render(request, "home.html")

def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    return HttpResponse(f"<h2>Name: {name} Age: {age}</h2>")
