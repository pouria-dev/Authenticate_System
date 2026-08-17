from django.shortcuts import render
# Create your views here.

from .forms import UserAuthenticationForm as loginform


def user_authentication_view(request):
    if request.method == "POST":

        form = loginform(request.POST)

        if not form.is_valid():
            return render( request , "" , {'form':form})

    return render(request , "" , {'form' : form})