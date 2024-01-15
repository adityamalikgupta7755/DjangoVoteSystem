from django.urls import path
from dasboardApp.views import *


urlpatterns = [
    path('', dashboardHome, name='dashboardHome'),
    path('dashboardlogin', dashboardlogin, name='dashboardlogin'),
    path('dashboardlogout', dashboardlogout, name='dashboardlogout'),
    path('dashboardAddProfile', dashboardAddProfile, name='dashboardAddProfile'),
    path('dashboardEditProfile/<Pid>',dashboardEditProfile, name="dashboardEditProfile"),
    path('dashboardUpdateProfilePic/<Pid>',dashboardUpdateProfilePic, name="dashboardUpdateProfilePic"),

    path('dashboardMaleProfile', dashboardMaleProfile, name='dashboardMaleProfile'),
    path('dashboardFemaleProfile', dashboardFemaleProfile, name='dashboardFemaleProfile'),


    path('dashboardResult', dashboardResult, name='dashboardResult'),


    path('dashboardSendInvite', dashboardSendInvite, name='dashboardSendInvite'),

    path('dashboardAddMailtemplate', dashboardAddMailtemplate, name='dashboardAddMailtemplate'),
    path('dashboardEditMailtemplate/<Mid>', dashboardEditMailtemplate, name='dashboardEditMailtemplate'),



    path('dashboardCreateInvite', dashboardCreateInvite, name='dashboardCreateInvite'),
    path('dashboardDelBatach/<Bid>', dashboardDelBatach, name='dashboardDelBatach'),



    path('dashboardInvitation/<Bid>', dashboardInvitation, name='dashboardInvitation'),
]
