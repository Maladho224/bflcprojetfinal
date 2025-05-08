from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    
    return render(request,'index.html')
def services(request):
    req =Services.objects.all()
    return render(request,'service.html',{'req':req})
def photo(request):
    req = Albums.objects.order_by('date_aj')[:5]
    return render(request,'photos.html',{'req':req})
def activites(request):
    req= Activites.objects.order_by('date_aj')[:5]
    return render(request, 'activites.html',{'req':req})
def contact(request):
    if request.method =="POST":
        form =FormContact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form= FormContact()
           
    return render(request, 'contact.html',{'form':form})
