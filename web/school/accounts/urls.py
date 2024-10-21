
from django.urls import path
from .views import user_logout,user_login

urlpatterns= [
    path ("login/",user_login ,name="login"),
    path ("logout/",user_logout ,name="logout"),
]