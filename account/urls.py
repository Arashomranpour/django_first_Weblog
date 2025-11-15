from django.urls import path
from . import views

app_name="account_app"
urlpatterns = [
    path("login",views.mylogin,name="login"),
    path("logout",views.mylogout,name="logout"),
    path("register",views.myregister,name="register"),
    path("edit",views.edit_user,name="edit"),

]