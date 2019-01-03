import base64

from django.contrib.auth.models import User

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from ..models import Light

class TestSearchLocations(APITestCase):
    fixtures = ['test_views.json']

    def setUp(self):
        # Basic認証を通すための処理
        self.username = ''
        self.password = ''

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
        self.username = ''
        self.password = ''

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