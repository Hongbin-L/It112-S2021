from django.test import TestCase
from .models import Meeting, Minute, Resource, Event
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
from django.utils import timezone
from .views import newResource
from .forms import ResourceForm

# Create your tests here.
class MeetingTest(TestCase):
    def test_string(self):
        met = Meeting(title='meeting')
        self.assertEqual(str(met), met.title)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'Meeting')

class MinuteTest(TestCase):
    def test_string(self):
        testMin = Minute(text='Minute')
        self.assertEqual(str(testMin), testMin.text)

    def test_table(self):
        self.assertEqual(str(Minute._meta.db_table), 'Minute')


class EventTest(TestCase):

    def test_string(self):
        testEvent = Event(title='Event')
        self.assertEqual(str(testEvent), testEvent.title)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'Event')

class ResourceTest(TestCase):
    def setup(self):
        testUser = User(username='Hongbin')
        testResource = Resource(name='Restest',type='photo',URL='https://www.pexels.com/',description='Pexels Free Photo',userid=testUser,date=datetime.date(2021,5,25))
        return testResource

    def test_string(self):
        testResource = self.setup()
        self.assertEqual(str(testResource), testResource.name)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'Resource')

# Testing
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class GetMeetingTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('getMeeting'))
        self.assertEqual(response.status_code, 200)


class MeetingDetailsTest(TestCase):
    def setUp(self):
        self.meeting1 = Meeting.objects.create(
            title='To prevent the flu',
            date=datetime.datetime.now(tz=timezone.utc),
            time=datetime.time(10, 33, 45),
            location='The library at Seattle downtown',
            Agenda="Should we wear mask and keep  Social distance")

        self.meeting2 = Meeting.objects.create(
            title='watching football',
            date=datetime.datetime.now(tz=timezone.utc),
            time=datetime.time(10, 33, 40),
            location='at home',
            Agenda="watching football")

    def test_meeting_details_success(self):
        response = self.client.get(
        reverse('meetingDetails', args=(self.meeting1.id,)))
        self.assertEqual(response.status_code, 200)

    def test_number_of_meeting(self):
        meetingCount = Meeting.objects.count()
        self.assertEqual(meetingCount, 2)

    class FormTest(TestCase):
        def setUpTestData(cls):
            cls.testUser = User.objects.create(
                username='userOne', password="p@ssw0rd1")

        def test_resource_form_request_login(self):
            response = self.client.get('/club/newResource')
            self.assertRedirects(
                response, '/accounts/login/?next=/club/newResource')

        def test_resource_form_is_valid(self):
            form = ResourceForm(
                data={'name': "test_resource",
                    'type': "test type",
                    "URL": "www.test.com",
                    "description": "test description",
                    "userid": self.testUser,
                    "date": "2021-06-01"})
            self.assertTrue(form.is_valid())

        def test_resource_form_templates_used(self):
            # login
            self.client.force_login(self.testUser)
            response = self.client.get('/club/newResource')
            self.assertTemplateUsed("club/newResource.html")

        def test_resource_form_templates_context(self):
            # login
            self.client.force_login(self.testUser)
            response = self.client.get('/club/newResource')
            self.assertFalse(response.context["isSaveOne"])
            form = ResourceForm()
            self.assertContains(response, form.as_table())

        def test_resource_form_view(self):
            self.client.force_login(self.testUser)
            response = self.client.get('/club/newResource')
            self.assertEqual(response.resolver_match.func, newResource)