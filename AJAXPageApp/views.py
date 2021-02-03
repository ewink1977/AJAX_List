from django.core.paginator import Paginator
from django.shortcuts import render, redirect
import datetime
from .models import User

def displayMainPage(request):
    users = User.objects.all()
    paginator = Paginator(users.order_by('id'), 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'html/main.html', context)

def updateUserList(request):
    nameUpdate = User.objects.filter(first_name = request.POST['firstname'])
    paginator = Paginator(nameUpdate.order_by('id'), 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'html/return.html', context)
