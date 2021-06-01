from django.shortcuts import get_object_or_404, render
from .models import Resource, Meeting
from .forms import MeetingForm, ResourceForm

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def getResource(request):
    res = Resource.objects.all()
    return render(request, 'club/Resource.html', {"Resource": res})

def getMeeting(request):
    met = Meeting.objects.values('id', 'title')
    return render(request, 'club/Meeting.html', {"Meetings": met})

def meetingDetails(request, id):
    details = get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meetingDetails.html', {"details": details})

def newResource(request):
    isSaveOne = False
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            newres = form.save()
            isSaveOne = True
    form = ResourceForm()
    return render(request, 'club/newResource.html', {'form': form, 'isSaveOne': isSaveOne})


def newMeeting(request):
    isSaveOne = False
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            newmet = form.save()
            isSaveOne = True
    form = MeetingForm()
    return render(request, 'club/newMeeting.html', {'form': form, "isSaveOne": isSaveOne})