from django.shortcuts import render

def landing_page(request):
    return render(request, 'landingpage/landing_page.html')


# Create your views here.
