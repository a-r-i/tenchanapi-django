import base64

from django.contrib.auth.models import User

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from ..models import Light, Body, SleepSummary, Sleep, NokiahealthapiToken, Heartrate

class TestSearchLocations(APITestCase):
    fixtures = ['test_views.json']

    def setUp(self):
        # Basic認証を通すための処理
        self.username = 'username'
        self.password = 'password'

        self.c = APIClient(HTTP_USER_AGENT='test_agent')
        self.c.user = User(username=self.username)
        self.c.user.set_password(self.password)
        self.c.user.save()

        self.username_password = '%s:%s' % (self.username, self.password)
        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode(self.username_password.encode()).decode(),
        }

    def test_post(self):
        # 新宿駅の緯度と経度
        data = {
                'latitude': 35.6895924,
                'longitude': 139.7004131
                }

        response = self.c.post('/locations/search/', data, **self.auth_headers)
        self.assertEqual(response.status_code, 200)


class LightTests(APITestCase):
    fixtures = ['test_views.json']

    def setUp(self):
        # Basic認証を通すための処理
        self.username = 'username'
        self.password = 'password'

        self.c = APIClient(HTTP_USER_AGENT='test_agent')
        self.c.user = User(username=self.username)
        self.c.user.set_password(self.password)
        self.c.user.save()

        self.username_password = '%s:%s' % (self.username, self.password)
        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode(self.username_password.encode()).decode(),
        }

    def test_create_light(self):
        data = {
                'timestamp': 1,
                'member': 1,
                'device': 'test_device',
                'sensor': 'test_sensor',
                'light': 1
                }

        self.assertEqual(Light.objects.count(), 1)
        response = self.c.post('/lights/', data, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Light.objects.count(), 2)

    def test_read_light(self):
        response = self.c.get('/lights/', **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BodyTests(APITestCase):
    fixtures = ['test_views.json']

    def setUp(self):
        # Basic認証を通すための処理
        self.username = 'username'
        self.password = 'password'

        self.c = APIClient(HTTP_USER_AGENT='test_agent')
        self.c.user = User(username=self.username)
        self.c.user.set_password(self.password)
        self.c.user.save()

        self.username_password = '%s:%s' % (self.username, self.password)
        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode(self.username_password.encode()).decode(),
        }

    def test_create_body(self):
        data = {
                'timestamp': 1,
                'member': 1,
                'muscle_mass': 1,
                'hydration': 1,
                'bone_mass': 1,
                'device': 'test_device',
                }

        self.assertEqual(Body.objects.count(), 1)
        response = self.c.post('/bodies/', data, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Body.objects.count(), 2)

    def test_read_body(self):
        response = self.c.get('/bodies/', **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SleepSummaryTests(APITestCase):
    fixtures = ['test_views.json']

    def setUp(self):
        # Basic認証を通すための処理
        self.username = 'username'
        self.password = 'password'

        self.c = APIClient(HTTP_USER_AGENT='test_agent')
        self.c.user = User(username=self.username)
        self.c.user.set_password(self.password)
        self.c.user.save()

        self.username_password = '%s:%s' % (self.username, self.password)
        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode(self.username_password.encode()).decode(),
        }

    def test_create_sleepsummary(self):
        data = {
                'member': 1,
                'startdate': 1,
                'enddate': 1,
                'wakeupduration': 1,
                'lightsleepduration': 1,
                'deepsleepduration': 1,
                'remsleepduration': 1,
                'durationtosleep': 1,
                'durationtowakeup': 1,
                'wakeupcount': 1,
                'device': 'test_device',
                }

        self.assertEqual(SleepSummary.objects.count(), 1)
        response = self.c.post('/sleepsummaries/', data, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SleepSummary.objects.count(), 2)

    def test_read_sleepsummary(self):
        response = self.c.get('/sleepsummaries/', **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SleepTests(APITestCase):
    fixtures = ['test_views.json']

    def setUp(self):
        # Basic認証を通すための処理
        self.username = 'username'
        self.password = 'password'

        self.c = APIClient(HTTP_USER_AGENT='test_agent')
        self.c.user = User(username=self.username)
        self.c.user.set_password(self.password)
        self.c.user.save()

        self.username_password = '%s:%s' % (self.username, self.password)
        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode(self.username_password.encode()).decode(),
        }

    def test_create_sleep(self):
        data = {
                'member': 1,
                'sleep_level': 1,
                'startdate': 1,
                'enddate': 1,
                'device': 'test_device',
                'registered_at': 1,
                'timestamp': '1'
                }

        self.assertEqual(Sleep.objects.count(), 1)
        response = self.c.post('/sleeps/', data, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sleep.objects.count(), 2)

    def test_read_sleep(self):
        response = self.c.get('/sleeps/', **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class NokiahealthapiTokenTests(APITestCase):
    fixtures = ['test_views.json']

    def setUp(self):
        # Basic認証を通すための処理
        self.username = 'username'
        self.password = 'password'

        self.c = APIClient(HTTP_USER_AGENT='test_agent')
        self.c.user = User(username=self.username)
        self.c.user.set_password(self.password)
        self.c.user.save()

        self.username_password = '%s:%s' % (self.username, self.password)
        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode(self.username_password.encode()).decode(),
        }

    def test_create_nokiahealthapitoken(self):
        data = {
                'member': 1,
                'access_token': '1',
                'refresh_token': '1'
                }

        self.assertEqual(NokiahealthapiToken.objects.count(), 1)
        response = self.c.post('/nokiahealthapi_tokens/', data, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(NokiahealthapiToken.objects.count(), 2)

    def test_read_nokiahealthapitoken(self):
        response = self.c.get('/nokiahealthapi_tokens/', **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class HeartrateTests(APITestCase):
    fixtures = ['test_views.json']

    def setUp(self):
        # Basic認証を通すための処理
        self.username = 'username'
        self.password = 'password'

        self.c = APIClient(HTTP_USER_AGENT='test_agent')
        self.c.user = User(username=self.username)
        self.c.user.set_password(self.password)
        self.c.user.save()

        self.username_password = '%s:%s' % (self.username, self.password)
        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode(self.username_password.encode()).decode(),
        }

    def test_create_heartrate(self):
        data = {
                'timestamp': 1,
                'member': 1,
                'bpm': 1,
                'device': 'test_device'
                }

        self.assertEqual(Heartrate.objects.count(), 1)
        response = self.c.post('/heartrates/', data, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Heartrate.objects.count(), 2)

    def test_read_heartrate(self):
        response = self.c.get('/heartrates/', **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)