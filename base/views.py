from django.shortcuts import render
from .models import Profile, Skills
from django.core.mail import send_mail
# Create your views here.


def index(request):

    profile = Profile.objects.all()

    skills = Skills.objects.all()

    context = {
        'profile': profile,
        'skills': skills,
    }

    if request.method == 'POST':
        Name = request.POST['Name']
        Email = request.POST['Email']
        Message = request.POST['Message'] + '  ' + Email
        send_mail(
            Name,
            Message,
            Email,
            ['josphat.gitogo@gmail.com']
        )
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html', context)
