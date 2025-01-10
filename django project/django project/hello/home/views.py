from django.shortcuts import render, HttpResponse
from home.models import contact
from django.contrib import messages
from django.views.generic import TemplateView
# Create your views here.

#class HomeView(TemplateView):
 #   template_name = 'home.html'

def index(request):
    context={
        'variable1':'this is sent',
        'variable2':'hi'    
      }
    return render(request, 'index.html',context)
    return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html',)
    return HttpResponse("this is abo utpage")

def services(request):
    return render(request, 'services.html',)
    return HttpResponse("this is servicepage")

def contact(request):
    if request.method == "POST":
        name=request.POST.get('email')
        name=request.POST.get('password')
        contact=contact(email=email, password=password)
        contact.save()
        messages.success(request, "Your mesage has been sent.")
    return render(request, 'contact.html',)
    return HttpResponse("this is contactpage")