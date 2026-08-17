# Write you're forms here


from django import forms

# Source - https://stackoverflow.com/a/1962289
# Posted by SapphireSun
# Retrieved 2026-08-17, License - CC BY-SA 2.5

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class UserAuthenticationForm(forms.Form):
    email = forms.EmailField(max_length=30, required=True)
    password = forms.CharField(max_length=30, required=True , widget=forms.PasswordInput()) 



    # Handling non_field error here

    def clean(self): 
        cleaned_data = super().clean() # Run clean method from Parent class with super method

        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password : 

            user = authenticate( # authenticate function check user is exist or not 
                email = email ,
                  password = password
                  ) 

        if user is None: 
            raise ValidationError(_("Password or email not correct"))

        self.user = user

        return cleaned_data



