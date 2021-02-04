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
    first = request.POST['firstname']
    last = request.POST['lastname']
    startDate = request.POST['startdate']
    endDate = request.POST['enddate']
    nameUpdate = User.objects.filter(first_name__icontains=first, last_name__icontains=last, birthdate__range=(startDate, endDate))
    paginator = Paginator(nameUpdate.order_by('id'), 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'html/return.html', context)
