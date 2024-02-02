from django.shortcuts import render
from django.http import HttpResponse
#возвращаем значение выполнения функции - вызов нужного html-шаблона
def choto(request):
    return render(request, 'timetable/npf.html')

