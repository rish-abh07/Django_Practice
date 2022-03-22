from django.shortcuts import render 
from hoe.models import Contact

# Create your views here.

def index(request):
  
    return render(request , 'test.html' )

def aboutus(request):
  
     return render(request , 'aboutus.html' )

def contact(request):
        if request.method=="POST":
            name =request.POST.get('name')
            email=request.POST.get('email')
            suggest=request.POST.get('suggestion')
            contact=Contact(name=name,email=email,suggestion=suggest)
            contact.save()
        return render(request , 'contactus.html' )

