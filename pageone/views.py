from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from . models import ContactForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages


# Create your views here.
def HomePage(request):
    template_name = 'index.html'
    return render(request, template_name)

def contact(request):
    template_name = 'contact.html'
    if request.method == "POST":
        contact = ContactForm()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact.name = name
        contact.email =email
        contact.subject = subject
        contact.message = message
        contact.save()
        messages.success(request, 'Message has been Sent Successfully!')
        return render(request, template_name)
    else:
        return render(request, template_name)







