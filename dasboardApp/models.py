
from django.db import models
import uuid
# Create your models here.
class Gender_Table(models.Model):
    Gender  = models.CharField(max_length=200)
    Created_Date_Time = models.DateField(auto_now=False, auto_now_add=True, blank=True )
    Modified_Date_Time = models.DateField(auto_now=True, auto_now_add=False, blank=True)

    def __str__(self):
        return self.Gender

class Mail_Tempalte(models.Model):
    Name  = models.CharField(max_length=200)
    Subject  = models.CharField(max_length=200)
    body  = models.TextField(null=True,blank=True)
    Created_Date_Time = models.DateField(auto_now=False, auto_now_add=True, blank=True )
    Modified_Date_Time = models.DateField(auto_now=True, auto_now_add=False, blank=True)

    def __str__(self):
        return self.Name
    
    

class BatchInvite(models.Model):
    Batch  = models.CharField(max_length=200)
    Batch_list = models.TextField(null=True,blank=True)
    Batch_Template =models.ForeignKey(Mail_Tempalte, null=True, on_delete=models.SET_NULL)
    Batch_Send = models.BooleanField(default=False)
    Created_Date_Time = models.DateField(auto_now=False, auto_now_add=True, blank=True )
    Modified_Date_Time = models.DateField(auto_now=True, auto_now_add=False, blank=True)
    def __str__(self):
        return self.Batch



class Pofile(models.Model):
    Pofile_Id = models.UUIDField(default=uuid.uuid4, editable=False)
    Pofile_Name = models.CharField(max_length=200)
    Pofile_dsc = models.CharField(max_length=400)
    Pofile_Email = models.CharField(max_length=400)
    Pofile_Gender =models.ForeignKey(Gender_Table, null=True, on_delete=models.SET_NULL)
    Pofile_Point = models.IntegerField(null=True, default=0)
    Pofile_Pic = models.ImageField(upload_to ='uploads/')
    Pofile_flag = models.BooleanField(default=False)
    Pofile_competitor = models.BooleanField(default=False)
    Pofile_Created_Date_Time = models.DateField(auto_now=False, auto_now_add=True )
    Pofile_Modified_Date_Time = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.Pofile_Name

class SendInvite(models.Model):
    SendInvite_Id = models.UUIDField(default=uuid.uuid4, editable=False)
    SendInvite_user =models.ForeignKey(Pofile, null=True, on_delete=models.SET_NULL)
    SendInvite_Batch =models.ForeignKey(BatchInvite, null=True, on_delete=models.CASCADE)
    SendInvite_link = models.CharField(max_length=200)
    SendInvite_Active = models.BooleanField(default=False)
    SendInvite_Created_Date_Time = models.DateField(auto_now=False, auto_now_add=True )
    SendInvite_Modified_Date_Time = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"{self.SendInvite_user}"
    


