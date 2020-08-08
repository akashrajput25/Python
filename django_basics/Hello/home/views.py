from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse('This is homepage')

def about(request):
    return HttpResponse('This is aboutpage')
    
def services(request):
    return HttpResponse('This is service page')

def about(request):
    return HttpResponse('This is about page')