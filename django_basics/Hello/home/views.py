from django.shortcuts import render,HttpResponse

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
    return render(request,'contact.html')

def skills(request):
    return render(request,'skills.html')

