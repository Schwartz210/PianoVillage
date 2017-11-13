from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

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
    return render(request, 'piano_app/members.html')

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
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'piano_app/signup.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def sponsors(request):
    return render(request, 'piano_app/sponsors.html')

def thankyou(request):
    return render(request, 'piano_app/thankyou.html')
