from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMessage
from django.contrib import messages

def home(request):
    return render(request, 'maritime/home.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message'],
            )
            messages.success(request, 'Your message has been sent! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'maritime/contact.html', {'form': form})