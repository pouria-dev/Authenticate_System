from .views import user_authentication_view as login_view
from django.urls import path


app_name = "user"
urlpatterns = [
    path("login/" , login_view, name="login")
]
