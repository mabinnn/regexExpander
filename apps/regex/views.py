from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'regex/home.html')



def expand(request):
    return render(request, 'regex/regex.html')
