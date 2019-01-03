import base64

from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient

class TestSearchLocations(APITestCase):
    fixtures = ['test_views.json']

    def setUp(self):
        self.username = ''
        self.password = ''

        self.c = APIClient(HTTP_USER_AGENT='test_agent')
        self.c.user = User(username=self.username)
        self.c.user.set_password(self.password)
        self.c.user.save()

        # 新宿駅の緯度と経度
        self.data = {
            'latitude': 35.6895924,
            'longitude': 139.7004131
        }

    def test_post(self):
        username_password = '%s:%s' % (self.username, self.password)
        auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode(username_password.encode()).decode(),
        }

        response = self.c.post('/locations/search', self.data, **auth_headers)
        self.assertEqual(response.status_code, 200)