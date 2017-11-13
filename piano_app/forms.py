from django import forms
from django.contrib.auth.models import User
from piano_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfo(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('date_of_birth',
                  'sex',
                  'school_name',
                  'grade',
                  'address1',
                  'address2',
                  'city',
                  'state',
                  'zip_code',
                  'phone',
                  'email',
                  'volunteer_experience',
                  'interest_in_piano_village',
                  'goals_for_service_to_the_community',
                  'emergency_name',
                  'emergency_phone',
                  'relationship',
                  'how_did_you_hear_about_us')
