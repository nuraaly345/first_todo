from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request, 'homepage.html')


def test(request):
    return render(request, 'test.html')

def check(request):
    return HttpResponse(request, 'Gitти жаңылоо')
