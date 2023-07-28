from .models import SignUpModel
from django import forms



class  UserForm(forms.ModelForm):
    class Meta :
        model=SignUpModel
        field='__all__'