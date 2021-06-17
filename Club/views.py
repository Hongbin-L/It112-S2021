from django.shortcuts import get_object_or_404, render
from .models import Resource, Meeting
from .forms import MeetingForm, ResourceForm
from django.contrib.auth.decorators import login_required

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


@login_required
def newMeeting(request):
    isSaveOne = False
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            newmet = form.save()
            isSaveOne = True
    form = MeetingForm()
    return render(request, 'club/newMeeting.html', {'form': form, "isSaveOne": isSaveOne})

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')