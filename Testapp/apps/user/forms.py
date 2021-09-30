from django import forms
from django.db.models import fields
from .models import User

class UserForm(forms.ModelForm):
    
    confirmed_pw = forms.CharField(max_length=255)
    
    class Meta:
        model = User
        fields = '__all__'

    def clean(self):
        
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get('confirmed_pw')

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )