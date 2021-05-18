from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')


def test(request):
    return render(request, 'test.html')
