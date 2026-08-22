from django.shortcuts import render , redirect
# Create your views here.
from django.http import HttpResponse
from .forms import UserAuthenticationForm as loginform
from django.urls import reverse

def user_authentication_view(request):
    if request.method == "POST":

        form = loginform(request.POST)

        if form.is_valid():
            return redirect("/")
    else:
        form = loginform()

    return render( request , "account/authenticate.html" , {'form':form})

    
