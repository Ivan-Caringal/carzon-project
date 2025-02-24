from django.shortcuts import render
from .models import Team


# Create your views here.
def home(request):
    teams = Team.objects.all()
    
    data = {
        'teams': teams,
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
