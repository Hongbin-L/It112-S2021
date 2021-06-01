from .models import Meeting, Resource
from django.forms import ModelForm


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'


class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'
        labels = {
            "userid": "Create by"
        }