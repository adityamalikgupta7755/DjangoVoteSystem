from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.http import HttpResponseRedirect, HttpResponse
# from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Pofile,Gender_Table, SendInvite, BatchInvite, Mail_Tempalte
from .forms import Add_Pofile_form, Edit_Pofile_form, Update_PofilePic_form, AddEmailTemplate_form, BatchInvite_form, EditEmailTemplate_form

# Create your views here.
@login_required(redirect_field_name='next', login_url='dashboardlogin')
def dashboardHome(request):
    genderlist = Gender_Table.objects.all()
    userobj= Pofile.objects.all()
    return render(request, 'dasboardApp\dasboardHome.html',{
        'userobj':userobj,
        'genderlist':genderlist,
    })

@login_required(redirect_field_name='next', login_url='dashboardlogin')
def dashboardMaleProfile(request):
    userobj= Pofile.objects.filter(Pofile_Gender=Gender_Table.objects.get(Gender='Male'))
    return render(request, 'dasboardApp\dashboardMaleProfile.html',{
        'userobj':userobj,
    })

@login_required(redirect_field_name='next', login_url='dashboardlogin')
def dashboardFemaleProfile(request):
    userobj= Pofile.objects.filter(Pofile_Gender=Gender_Table.objects.get(Gender='Female'))
    return render(request, 'dasboardApp\dashboardFemaleProfile.html',{
        'userobj':userobj,
    })

@login_required(redirect_field_name='next', login_url='dashboardlogin')
def dashboardAddProfile(request):
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
            return redirect('dashboardAddProfile')
           
    else:
        form =  Add_Pofile_form(request.POST, request.FILES)
    return render(request, 'dasboardApp\dashboardAddProfile.html',{'form':form,})

@login_required(redirect_field_name='next', login_url='dashboardlogin')
def dashboardEditProfile(request, Pid):
    userobj= Pofile.objects.get(Pofile_Id=Pid)
    form = Edit_Pofile_form(request.POST or None,   instance=userobj)
    form2 = Update_PofilePic_form(request.POST,request.FILES,instance = userobj)
    if request.method == "POST":
        if all([form.is_valid(), form2.is_valid()]):
            form.save()
            form2.save()
            messages.success(request, 'Profile Updated & Saved')
            return redirect(dashboardHome)
        else:
            form
    return render(request, 'dasboardApp\dashboardEditProfile.html',{
        'form':form,
        'form2':form2,})

@login_required(redirect_field_name='next', login_url='dashboardlogin')
def dashboardUpdateProfilePic(request, Pid):
    userobj= Pofile.objects.get(Pofile_Id=Pid)
    form = Update_PofilePic_form(request.POST or None, request.FILES,  instance=userobj)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated & Saved')
            return redirect(dashboardHome)
        else:
            form
    return render(request, 'dasboardApp\dashboardUpdateProfilePic.html',{
        'form':form,})

@login_required(redirect_field_name='next', login_url='dashboardlogin')
def dashboardResult(request):
    FemaleUserlist = []
    FemaleUserPoint = []
    MaleUserlist = []
    MaleUserPoint = []
    femaleuserobj= Pofile.objects.filter(Pofile_Gender=Gender_Table.objects.get(Gender='Female')).values('Pofile_Name','Pofile_Point', 'Pofile_competitor')
    for Fuser in femaleuserobj:
        if Fuser['Pofile_competitor']:
            FemaleUserlist.append(str(Fuser['Pofile_Name']))
            FemaleUserPoint.append(int(Fuser['Pofile_Point']))


    Maleuserobj= Pofile.objects.filter(Pofile_Gender=Gender_Table.objects.get(Gender='Male')).values('Pofile_Name','Pofile_Point', 'Pofile_competitor')
    for Fuser in Maleuserobj:
        if Fuser['Pofile_competitor']:
            MaleUserlist.append(str(Fuser['Pofile_Name']))
            MaleUserPoint.append(int(Fuser['Pofile_Point']))

    
   
    return render(request, 'dasboardApp\dashboardResult.html',{
        'FemaleUserlist':FemaleUserlist,
        'FemaleUserPoint':FemaleUserPoint,
        'MaleUserlist':MaleUserlist,
        'MaleUserPoint':MaleUserPoint,
    })

@login_required(redirect_field_name='next', login_url='dashboardlogin')
def dashboardAddMailtemplate(request):
    mailtempalte = Mail_Tempalte.objects.all()
    print("mailtempalte",mailtempalte)
    form =  AddEmailTemplate_form(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Email template Saved')
            return redirect('dashboardAddMailtemplate')
        else:
            form
    return render(request, 'dasboardApp\dashboardAddMailtemplate.html',{
        'form':form,
        'mailtempalte':mailtempalte,
    })

@login_required(redirect_field_name='next', login_url='dashboardlogin')
def dashboardEditMailtemplate(request, Mid):
        Mailobj= Mail_Tempalte.objects.get(id=Mid)
        form = EditEmailTemplate_form(request.POST or None,   instance=Mailobj)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, 'Email template Edited Saved')
                return redirect('dashboardAddMailtemplate')
            else:
                form
        return render(request, 'dasboardApp\dashboardEditMailtemplate.html',{
        'form':form,
    })

@login_required(redirect_field_name='next', login_url='dashboardlogin')
def dashboardCreateInvite(request):
    userobj= Pofile.objects.all()
    form = BatchInvite_form(request.POST)
    userlist=[]
    if request.method == "POST":
        if form.is_valid():
            forms = form.save(commit=False)
            forms.Batch_list =userlist
            forms.save()
            for user in request.POST.getlist('user'):
                userlist.append(user)
                sendinviteobj = SendInvite(
                    SendInvite_user=Pofile.objects.get(Pofile_Id=user),
                    SendInvite_Batch=forms,
                           )
                sendinviteobj.SendInvite_link=f"http://{request.get_host()}/GSS/{sendinviteobj.SendInvite_Id}"
                sendinviteobj.save()

            messages.success(request, 'Batch Created')
            return redirect('dashboardSendInvite')
        else:
            form
    # print("userlist", userlist)
    return render(request, 'dasboardApp\dashboardCreateInvite.html',{
        'form':form,
        'userobj':userobj,
    })

@login_required(redirect_field_name='next', login_url='dashboardlogin')
def dashboardDelBatach(request, Bid):
    Batchobj = BatchInvite.objects.get(id=Bid)
    Batchobj.delete()
    messages.success(request, 'Batch  Deleted')
    return redirect('dashboardSendInvite')
    return render(request, 'dasboardApp\dashboardDelBatach.html',{'Batchobj':Batchobj,})

@login_required(redirect_field_name='next', login_url='dashboardlogin')
def dashboardSendInvite(request):
    Batchobj = BatchInvite.objects.filter(Batch_Send=False)
    SendInviteobj = SendInvite.objects.all()
    return render(request, 'dasboardApp\dashboardSendInvite.html',{
        'Batchobj':Batchobj,
        'SendInviteobj':SendInviteobj,
    })

@login_required(redirect_field_name='next', login_url='dashboardlogin')
def dashboardInvitation(request, Bid):
    SIList = []
    Batchobj = BatchInvite.objects.get(id=Bid)
    SendInviteobj = SendInvite.objects.filter(SendInvite_Batch=Batchobj)
    for obj in SendInviteobj:
        print("----------------------------")
        print("SendInvite_Id", obj.SendInvite_Id)
        print("SendInvite_user", obj.SendInvite_user)
        SIList.append(obj.SendInvite_user)
        print("SendInvite_Batch", obj.SendInvite_Batch)
        print("SendInvite_link", obj.SendInvite_link)
        print("SendInvite_Active", obj.SendInvite_Active)
        print("SendInvite_Created_Date_Time", obj.SendInvite_Created_Date_Time)
        print("SendInvite_Modified_Date_Time", obj.SendInvite_Modified_Date_Time)
        print("----------------------------")

    Batchobj.Batch_list=SIList
    Batchobj.Batch_Send=True
    Batchobj.save()
    return render(request, 'dasboardApp\dashboardInvitation.html',{
        'Batchobj':Batchobj,
        'SendInviteobj':SendInviteobj,
        })

def dashboardlogin(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST["username"],
                            password=request.POST["password"])
        if user:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('dashboardHome')
        else:
            messages.error(request, 'Logged in Fail')
    return render(request, 'dasboardApp\dashboardlogin.html')

@login_required(redirect_field_name='next', login_url='dashboardlogin')
def dashboardlogout(request):
    # Do some stuff...
    logout(request)
    return redirect('dashboardlogin')

    return render(request, 'dasboardApp\dashboardlogin.html')
