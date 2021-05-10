from django.shortcuts import render
from .models import Resource, Meeting

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def getResource(request):
    res = Resource.objects.all()
    return render(request, 'club/Resource.html', {"Resource": res})
