from django.shortcuts import render, redirect

def displayMainPage(request):
    return render(request, 'html/main.html')
