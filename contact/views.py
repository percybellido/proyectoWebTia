from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contact(request):
    contact_form=ContactForm()
    if request.method =="POST":
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            content=request.POST.get('contenido','')
            recipient_list=['pcbellido@hotmail.com']
            send_mail(name,email,content,recipient_list)
            return redirect(reverse('contact')+"?ok")
                            
            
    return render(request, 'contact/contact.html',{'form':contact_form})