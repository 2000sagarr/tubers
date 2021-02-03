from django.shortcuts import render
from .models import Slider, Team
from youtubers.models import Youtuber
# Create your views here.
#this methods are used in urls.py file
def home(request):
    # this will order slides according to created_date
    # sliders = Slider.objects.order_by('-created_date')
    # this is simple to grab all data
    sliders = Slider.objects.all()
    team = Team.objects.all()
    # filter data
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured = True)

    all_youtubers = Youtuber.objects.order_by('-created_date')
    # data is object by using we can fetch all the data
    data = {
        'sliders': sliders,
        'team' : team,
        'featured_youtubers' : featured_youtubers,
        'all_youtubers' :all_youtubers,
    }
    # data is passed to home page
    return render(request, 'webpages/home.html', data)
 
def about(request):
    return render(request, 'webpages/about.html')
    
def services(request):
    return render(request, 'webpages/services.html')
 
def contact(request):
    return render(request, 'webpages/contact.html')

