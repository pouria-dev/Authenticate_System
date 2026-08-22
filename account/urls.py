from .views import( user_authentication_view as login_view ,
                   user_creation_view as register_view)
from django.urls import path


app_name = "user"
urlpatterns = [
    path("login/" , login_view, name="login"),
    path("register/" , register_view , name="register")
]
