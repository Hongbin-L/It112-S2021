    
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=400)
    Agenda = models.CharField(max_length=400)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Meeting'
        verbose_name_plural = 'Meetings'


class Minute(models.Model):
    meetingid = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance = models.ManyToManyField(User)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'Minute'
        verbose_name_plural = 'Minutes'


class Resource(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    URL = models.CharField(max_length=100)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Resource'
        verbose_name_plural = 'Resources'


class Event(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=1000)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Event'
        verbose_name_plural = 'Events'