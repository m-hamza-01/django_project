from django.urls import path
from . import views 

urlpatterns = [
    path ('bye/', views.say_hello, name='say_hello')
]