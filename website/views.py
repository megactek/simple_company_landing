from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', context={
        'active': 'current',
    })

def about(request):
    return render(request, 'about.html', context={
        'active': 'current',
    })

def services(request):
    return render(request, 'services.html', context={
        'active': 'current',
        })