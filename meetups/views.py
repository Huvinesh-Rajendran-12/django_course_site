from meetups.forms import RegistrationForm
from django.shortcuts import render, redirect 

from .models import Meetup , participant
from .forms import RegistrationForm

# Create your views here.

def welcome(request):
    meetups = Meetup.objects.all()
    return render(request,'meetups/welcome.html',{
        'meetups':meetups
    })

def meetup_details(request,meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registrationForm = RegistrationForm
           
        else:
            registrationForm = RegistrationForm(request.POST)
            if registrationForm.is_valid():
                usr_email = registrationForm.cleaned_data['email']
                Participant, _ = participant.objects.get_or_create(email=usr_email)
                selected_meetup.participants.add(Participant)
                return redirect('confirm-registration',meetup_slug=meetup_slug)
                
        return render(request,'meetups/detail.html',{
                'meetup_found':True,
                'meetup':selected_meetup,
                'form': registrationForm
            })
    except Exception as exc:
        return render(request, 'meetups/detail.html',
                      {'meetup_found':False})

def confirm_registration(request,meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request,'meetups/registration-success.html',{
        'organizer_email': meetup.organizer_email
    })