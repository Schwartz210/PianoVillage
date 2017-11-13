from django.db import models
from django.contrib.auth.models import User
from piano_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

# Create your models here.
class UserProfileInfoForm(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User)

    # Add any additional attributes you want
    date_of_birth = models.DateField(default='1987-04-27')
    SEX_CHOICES = (
        ('male','Male'),
        ('female','Female'),
        ('decline to identify','Decline to Identify')
    )
    sex = models.CharField(max_length=50, choices=SEX_CHOICES, default='decline to identify')
    school_name = models.CharField(max_length=50, default='Eshkol Academy')
    GRADE_CHOICES = (
        ('prek','Pre K'),
        ('kindergarten','Kindergarten'),
        ('first','First Grade'),
        ('second','Second Grade'),
        ('third','Third Grade'),
        ('forth','Fourth Grade'),
        ('fifth','Fifth Grade'),
        ('sixth','Sixth Grade'),
        ('seventh','Seventh Grade'),
        ('eighth','Eighth Grade'),
        ('ninth','Nineth Grade'),
        ('tenth','Tenth Grade'),
        ('eleventh','Eleventh Grade'),
        ('twelfth','Twelfth Grade'),
        ('adult','Adult'),
    )
    grade = models.CharField(max_length=50, choices=GRADE_CHOICES, default='prek')
    address1 = models.CharField(max_length=50, default='123 Fake St.')
    address2 = models.CharField(max_length=50, default='Apt 108')
    city = models.CharField(max_length=50, default='New York')
    state = models.CharField(max_length=50, default='New York')
    zip_code = models.CharField(max_length=5, default='12345')
    phone = models.CharField(max_length=10, default='9141234567')
    email = models.EmailField(max_length=200, default='example@gmail.com')
    volunteer_experience = models.TextField(max_length=5000, default='Previous volunteer experience')
    interest_in_piano_village = models.TextField(max_length=5000, default='I would like my child to learn how to play the piano')
    goals_for_service_to_the_community = models.TextField(max_length=5000, default='')
    emergency_name = models.CharField(max_length=10, default='John Smith')
    emergency_phone = models.CharField(max_length=10, default='9141234567')
    relationship = models.CharField(max_length=10, default='Father')
    HEAR_CHOICES = (
        ('friend','Friend'),
        ('parent','Parent'),
        ('website','Website'),
        ('media','Media'),
        ('other','Other'),
    )
    how_did_you_hear_about_us = models.CharField(max_length=50, choices=HEAR_CHOICES, default='media')

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
