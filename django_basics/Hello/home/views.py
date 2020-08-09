from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages

def index(request):
    context ={
        'variable' : "text here",
        'variable1' : 'hola'
    }
    
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
    
def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method =='post' or request.method =='POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        contact = Contact(firstname=firstname , lastname=lastname,email=email)
        contact.save()
        messages.success(request,'Thanks for contacting us!')
    return render(request,'contact.html')

def skills(request):
    return render(request,'skills.html')

