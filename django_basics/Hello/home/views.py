from django.shortcuts import render,HttpResponse

def index(request):
    context ={
        'variable' : "text here",
        'variable1' : 'hola'
    }
    return render(request,'index.html',context)

def about(request):
    return HttpResponse('This is aboutpage')
    
def services(request):
    return HttpResponse('This is service page')

def contact(request):
    return HttpResponse('This is contact page')