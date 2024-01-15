from django.urls import path
from VotingApp.views import *


urlpatterns = [
    path('', GSShome, name='GSShome'),
    path('GSS/<Rid>', GSS, name='GSS'),
    path('RegisterUser', RegisterUser, name='RegisterUser'),
    path('ThankyouPage', ThankyouPage, name='ThankyouPage'),
    path('MaleView/<Rid>', MaleView, name='MaleView'),
    path('FemaleView/<Rid>', FemaleView, name='FemaleView'),


    path('AlreadyReister', AlreadyReister, name='AlreadyReister'),
    path('ThankyouParticipation', ThankyouParticipation, name='ThankyouParticipation'),



]

