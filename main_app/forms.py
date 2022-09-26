from django import forms 
from .models import UserAccount, AudioData

class AccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields=  "__all__" 


class AudioDataForm(forms.ModelForm):
    class Meta:
        model = AudioData
        fields = "__all__"


