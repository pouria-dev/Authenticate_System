from django.shortcuts import render , redirect
# Create your views here.
from django.http import HttpResponse
from .forms import (UserAuthenticationForm as loginform,
                        UserCreationForm as registerform
                        )

from django.urls import reverse

def user_authentication_view(request):
    if request.method == "POST":

        form = loginform(request.POST)

        if form.is_valid():
            return redirect("/")
    else:
        form = loginform()

    return render( request , "account/authenticate.html" , {'form':form})

    

def user_creation_view(request):
    if request.method == "POST":
        form = registerform(request.POST)


        """
        form.cleaned_data returns a dictionary of validated form
        input fields and their values, 
        where string primary keys are returned as objects.
            
          """
        

        if form.is_valid():
        
            user = form.save(commit=False)

            user.set_password(form.cleaned_data["password2"])
            
            form.save()
            # using model form in forms.py so we can just save the form 

    else:
        form = registerform()

    return render(request , "account/creation.html", {'form':form})
