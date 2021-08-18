from django.shortcuts import render

from .models import Meetup

# Create your views here.

def welcome(request):
    meetups = Meetup.objects.all()
    return render(request,'meetups/welcome.html',{
        'meetups':meetups
    })

def meetup_details(request,meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        return render(request,'meetups/detail.html',{
            'meetup_found':True,
            'meetup_title':selected_meetup.title,
            'meetup_details':selected_meetup.description
        })
    except Exception as exc:
        return render(request, 'meetups/detail.html',
                      {'meetup_found':False})