from django.shortcuts import render
from django.core.mail import EmailMessage, send_mail, send_mass_mail
from django.conf import settings
from .forms import ContactForm


def homePage(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            subject = form.cleaned_data['subject']
            recipient = [form.cleaned_data['email'], ]
            message = form.cleaned_data['message']
            
            # message = request.POST.get('message')
            # subject = 'Welcome to Django Emailing'
            # messages = f'Hi there, Hope you are enjoying your django Tutorials. This is the message you dropped "{message}"'

        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient, fail_silently=False)
        return render(request, 'success.html', {'recipient_list': recipient})
    context = {'form': form}
    return render(request, 'index.html', context)