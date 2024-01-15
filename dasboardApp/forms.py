from django import forms
from django.forms import ModelForm
from .models import Pofile, Mail_Tempalte, BatchInvite


class Add_Pofile_form(ModelForm):
    class Meta :
        model = Pofile
        fields = {
            'Pofile_Name',
            'Pofile_dsc',
            'Pofile_Email',
            'Pofile_Gender',
            'Pofile_Pic',
            'Pofile_competitor',
        }
        widgets = {
            'Pofile_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Pofile_dsc':forms.Textarea(attrs={'class':'form-control', 'rows':'4'}), 
            'Pofile_Email':forms.EmailInput(attrs={'class':'form-control'}),
            'Pofile_Gender':forms.Select(attrs={'class':'form-select m-0 p-0'}), 
            'Pofile_Pic':forms.ClearableFileInput(attrs={'class':'btn btn-lg btn-primary'}),
            'Pofile_competitor':forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

class Edit_Pofile_form(ModelForm):
    class Meta :
        model = Pofile
        fields = {
            'Pofile_Name',
            'Pofile_dsc',
            # 'Pofile_Email',
            # 'Pofile_Gender',
            # 'Pofile_Pic',
            'Pofile_competitor',
        }
        widgets = {
            'Pofile_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Pofile_dsc':forms.Textarea(attrs={'class':'form-control', 'rows':'4'}), 
            # 'Pofile_Email':forms.EmailInput(attrs={'class':'form-control'}),
            # 'Pofile_Gender':forms.Select(attrs={'class':'form-select m-0 p-0'}), 
            # 'Pofile_Pic':forms.ClearableFileInput(attrs={'class':'btn btn-lg btn-primary'}),
            'Pofile_competitor':forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

class Update_PofilePic_form(ModelForm):
    class Meta :
        model = Pofile
        fields = {
            'Pofile_Pic',
        }
        widgets = {
            'Pofile_Pic':forms.ClearableFileInput(attrs={'class':'btn btn-lg btn-primary'}),
        }

class AddEmailTemplate_form(ModelForm):
    class Meta :
        model = Mail_Tempalte
        fields = {
            'Name',
            'Subject',
            'body',
        }
        widgets = {
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Subject':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control', 'rows':'4'}), 
        }



class EditEmailTemplate_form(ModelForm):
    class Meta :
        model = Mail_Tempalte
        fields = {
            'Name',
            'Subject',
            'body',
        }
        widgets = {
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Subject':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control', 'rows':'4'}), 
        }



class BatchInvite_form(ModelForm):
    class Meta :
        model = BatchInvite
        fields = {
            'Batch',
            'Batch_list',
            'Batch_Template',
        }
        widgets = {
            'Batch':forms.TextInput(attrs={'class':'form-control'}),
            'Batch_list':forms.Textarea(attrs={'class':'form-control', 'rows':'4'}), 
            'Batch_Template':forms.Select(attrs={'class':'form-select m-0 p-0'}), 
        }


