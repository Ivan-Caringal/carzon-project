from django.shortcuts import render
from .models import Team
from cars.models import Car


# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def contact(request):
    return render(request, 'pages/contact.html')

def services(request):
    return render(request, 'pages/service.html')


# filepath: /e:/coding/carzon-project/views.py
from django.shortcuts import render

def search(request):
    keyword = request.GET.get('keyword', '')  
    print("Keyword searched:", keyword)  # Debugging

    if keyword:
        results = Team.objects.filter(first_name__icontains=keyword)  
    else:
        results = Team.objects.none()  

    print("Results:", results)  # Debugging

    context = {
        'query': keyword,
        'results': results,
    }

    return render(request, 'base.html', context)  # Check this template name
