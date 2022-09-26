from django import forms 
from .models import UserAccount 

class AccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields=  "__all__" 


