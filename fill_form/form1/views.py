from django.shortcuts import render
from django.http import HttpResponse
from form1.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.


def index(request):
    context = {
                'var1':'here we go again.',
                'var2':'hello there!'
    }
    return render(request,'files/index.html',context)

def about(request):
    return render(request,'files/about.html')

def services(request):
    return render(request,'files/services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        text = request.POST.get('text')
        contact = Contact(name=name,email=email,phone=phone,text=text,date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')
    return render(request,'files/contact.html')
