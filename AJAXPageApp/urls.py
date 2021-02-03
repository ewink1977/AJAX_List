from django.urls import path
from . import views

urlpatterns = [
    path('', views.displayMainPage, name = 'displayMain'),
    path('update', views.updateUserList, name = 'updateList'),
]