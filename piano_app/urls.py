from django.conf.urls import url
from piano_app import views

app_name = 'piano_app'

urlpatterns = [
    url(r'^about',views.about, name='about'),
    url(r'^applications',views.applications, name='applications'),
    url(r'^base',views.base, name='base'),
    url(r'^community',views.community, name='community'),
    url(r'^competitions',views.competitions, name='competitions'),
    url(r'^contacts',views.contacts, name='contacts'),
    url(r'^donation',views.donation, name='donation'),
    url(r'^members',views.members, name='members'),
    url(r'^news',views.news, name='news'),
    url(r'^participation',views.participation, name='participation'),
    url(r'^philosophy',views.philosophy, name='philosophy'),
    url(r'^platform',views.platform, name='platform'),
    url(r'^prize',views.prize, name='prize'),
    url(r'^program',views.program, name='program'),
    url(r'^signup',views.signup, name='signup'),
    url(r'^sponsors',views.sponsors, name='sponsors'),
    url(r'^thankyou',views.thankyou, name='thankyou'),
]
