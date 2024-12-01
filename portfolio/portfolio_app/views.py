from django.shortcuts import render
from .models import Project, Skill
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email (configure settings for this)
            send_mail(
                f"Portfolio Contact: {form.cleaned_data['name']}",
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                [settings.EMAIL_HOST_USER],
            )
            form = ContactForm()  # Clear form on success

    return render(request, 'portfolio_app/home.html', {'projects': projects, 'skills': skills, 'form': form})
