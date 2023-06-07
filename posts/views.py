from django.shortcuts import HttpResponse, redirect
from datetime import date

# Create your views here.


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")


def redirect_to_youtube_view    (request):
    if request.method == 'GET':
        return redirect('https://www.youtube.com')


def now_date_view(request):
    if request.method == 'GET':
        return HttpResponse(f'Today is {date.today()}')


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodbye user!")



