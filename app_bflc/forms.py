from django import forms
import django.db
from .models import *

class FormContact(forms.ModelForm):
    class Meta:
        model = Message
        fields=['phone','email','subject','message']
        widgets={
           
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.EmailInput(attrs={'class':'form-control'}),
            'subject':forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.TextInput(attrs={'class':'form-control'}),
            
        }
class FormCommand(forms.ModelForm):
    class Meta:
        model = Commande
        fields=['engins','adres','phone']
        widgets={
           
            'engins':forms.TextInput(attrs={'class':'form-control'}),
            'adres':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            
            
        }
