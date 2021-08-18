from django.shortcuts import render

# Create your views here.

def welcome(request):
    meetups = [
        {'title': 'A First Meetup',
         'location': 'New York',
         'slug':'a-first-meetup'},
        {'title': 'A Second Meetup',
         'location':'Paris',
         'slug': 'a-second-meetup'},
        
    ]
    return render(request,'meetups/welcome.html',{
        'show_meetups':True,
        'meetups':meetups
    })

def meetup_details(request,meetup_slug):
    print(meetup_slug)
    selected_meetup = {'title': 'A First Meetup',
                       'description':'This is the first Meetup'}
    return render(request,'meetups/detail.html',{
        'meetup_title':selected_meetup['title'],
        'meetup_details':selected_meetup['description']
    })