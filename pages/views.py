from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def services(request):
    return render(request, 'pages/service.html')


# filepath: /e:/coding/carzon-project/views.py
from django.shortcuts import render

def search(request):
    query = request.GET.get('q')
    # Implement your search logic here
    context = {
        'query': query,
        # Add other context variables as needed
    }
    return render(request, 'search_results.html', context)