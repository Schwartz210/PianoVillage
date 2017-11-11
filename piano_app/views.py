from django.shortcuts import render
from django.conf.urls import url, include
# Create your views here.



def about(request):
    return render(request, 'piano_app/about.html')

def applications(request):
    return render(request, 'piano_app/applications.html')

def base(request):
    return render(request, 'piano_app/base.html')

def community(request):
    return render(request, 'piano_app/community.html')

def competitions(request):
    return render(request, 'piano_app/competitions.html')

def contacts(request):
    return render(request, 'piano_app/contacts.html')

def donation(request):
    return render(request, 'piano_app/donation.html')

def index(request):
    return render(request, 'piano_app/index.html')

def members(request):
    return render(request, 'piano_app/v.html')

def news(request):
    return render(request, 'piano_app/news.html')

def participation(request):
    return render(request, 'piano_app/participation.html')

def philosophy(request):
    return render(request, 'piano_app/philosophy.html')

def platform(request):
    return render(request, 'piano_app/platform.html')

def prize(request):
    return render(request, 'piano_app/prize.html')

def program(request):
    return render(request, 'piano_app/program.html')

def signup(request):
    return render(request, 'piano_app/signup.html')

def sponsors(request):
    return render(request, 'piano_app/sponsors.html')

def thankyou(request):
    return render(request, 'piano_app/thankyou.html')