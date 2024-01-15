from django.shortcuts import render, redirect
from dasboardApp.forms import Add_Pofile_form
# Create your views here.
from django.contrib import messages
from dasboardApp.models import Pofile,Gender_Table, SendInvite
def GSShome(request):
    return render(request, 'VotingApp\GSShome.html')



def RegisterUser(request):
    form =  Add_Pofile_form(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            Pofile_Name = form.cleaned_data.get("Pofile_Name")
            Pofile_Email = form.cleaned_data.get("Pofile_Email")
            Pofile_Gender = form.cleaned_data.get("Pofile_Gender")
            Pofile_dsc = form.cleaned_data.get("Pofile_dsc")
            Pofile_Pic = form.cleaned_data.get("Pofile_Pic")
            Pofile_competitor = form.cleaned_data.get("Pofile_competitor")
            form.save()
            messages.success(request, 'Profile Saved')
            return redirect('ThankyouPage')
           
    else:
        form =  Add_Pofile_form(request.POST, request.FILES)
    return render(request, 'VotingApp\RegisterUser.html',{'form':form,})


def GSS(request, Rid):
    rdiectlink=''
    invite = SendInvite.objects.get(SendInvite_Id=Rid)
    if invite.SendInvite_Active == False:
        userobj= Pofile.objects.get(Pofile_Id=invite.SendInvite_user.Pofile_Id)
        if str(userobj.Pofile_Gender) =='Male':
            rdiectlink=f"http://{request.get_host()}/FemaleView/{userobj.Pofile_Id}&1"
        if str(userobj.Pofile_Gender) =='Female':
            rdiectlink=f"http://{request.get_host()}/MaleView/{userobj.Pofile_Id}&1"
        invite.SendInvite_Active=True
        invite.save()
    else:
        return redirect('AlreadyReister')


    return render(request, 'VotingApp\GSS.html',{
        'Rid':Rid,
        'invite':invite,
        'userobj':userobj,
        'rdiectlink':rdiectlink,


        })

def MaleView(request, Rid):
    Rid =Rid.split('&')
    userobj= Pofile.objects.filter(Pofile_Gender=Gender_Table.objects.get(Gender='Male'))
    userobj = userobj.exclude(Pofile_Id=Rid[0])
    if request.method == "POST":
        radoption = request.POST['radoption']
        print("radoption",radoption)
        selecteduser = Pofile.objects.get(Pofile_Id=radoption)
        selecteduser.Pofile_Point= (selecteduser.Pofile_Point) + 10
        selecteduser.save()
        messages.success(request, 'you vote Saved for Male')
        print("Rid[1]",Rid[1])
        rdiectlink=f"http://{request.get_host()}/FemaleView/{Rid[0]}&2"
        if Rid[1] == '1':
            return redirect(rdiectlink)
        if Rid[1] == '2':
            return redirect('ThankyouParticipation')
    return render(request, 'VotingApp\MaleView.html',{
        'userobj':userobj,
        'Rid':Rid,
    })

def FemaleView(request, Rid):
    Rid =Rid.split('&')
    print("Rid[0]",Rid[0])
    print("Rid[1]",Rid[1])
    userobj= Pofile.objects.filter(Pofile_Gender=Gender_Table.objects.get(Gender='Female'))
    userobj = userobj.exclude(Pofile_Id=Rid[0])
    if request.method == "POST":
        radoption = request.POST['radoption']
        selecteduser = Pofile.objects.get(Pofile_Id=radoption)
        selecteduser.Pofile_Point= (selecteduser.Pofile_Point) + 10
        selecteduser.save()
        messages.success(request, 'you vote Saved for Female')
        rdiectlink=f"http://{request.get_host()}/MaleView/{Rid[0]}&2"
        if Rid[1] == '1':
            return redirect(rdiectlink)
        if Rid[1] == '2':
            return redirect('ThankyouParticipation')
    return render(request, 'VotingApp\FemaleView.html',{
        'userobj':userobj,
        'Rid':Rid,
    })


def ThankyouPage(request):
    return render(request, 'VotingApp\ThankyouPage.html')

def ThankyouParticipation(request):
    return render(request, 'VotingApp\ThankyouParticipation.html')

def AlreadyReister(request):
    return render(request, 'VotingApp\AlreadyReister.html')