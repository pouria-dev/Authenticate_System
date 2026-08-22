# Write you're forms here


from django import forms

# Source - https://stackoverflow.com/a/1962289
# Posted by SapphireSun
# Retrieved 2026-08-17, License - CC BY-SA 2.5

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import MyUser

class UserAuthenticationForm(forms.Form):
    email = forms.EmailField(max_length=30, required=True ,label="email")
    password = forms.CharField(max_length=30, required=True , label= "password", widget=forms.PasswordInput()) 



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


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField( max_length=20, required=True ,label="password1", widget=forms.PasswordInput)
    password2 = forms.CharField( max_length=20, required=True , label="password2", widget=forms.PasswordInput)
    class Meta:
        model = MyUser
        fields = ('email' ,'date_of_birth' )

        widgets=  {
            'date_of_birth' :  forms.SelectDateWidget()
        }

        # Source - https://stackoverflow.com/a/637020
        # Posted by Xbito
        # Retrieved 2026-08-22, License - CC BY-SA 2.5

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['email'].label = "Email"
            self.fields['date_of_birth'].lable = "date_of_birth"


    def clean(self):

        cleaned_data = super().clean()

        email = self.cleaned_data.get("email")
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        user = authenticate(email=email)
        if user :
            raise ValidationError("This email taked")

        if password1 != password2 :
            raise ValidationError("The passwords aren't same. ")
            

        
        # Source - https://stackoverflow.com/a/19222468
        # Posted by o3bvv, modified by community. See post 'Timeline' for change history
        # Retrieved 2026-08-22, License - CC BY-SA 4.0
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("Please enter a valid email address.")


        return cleaned_data