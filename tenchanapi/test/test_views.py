import base64

from django.contrib.auth.models import User

from rest_framework.test import APITestCase, APIClient

class SearchLocations(APITestCase):
    fixtures = ['test_views.json']

    def test_post(self):
        username = ''
        password = ''
        username_password = '%s:%s' % (username, password)

        c = APIClient(HTTP_USER_AGENT='test_agent')
        c.user = User(username=username)
        c.user.set_password(password)
        c.user.save()

        auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode(username_password.encode()).decode(),
        }

        # 新宿駅の緯度と経度
        data = {
            'latitude': 35.6895924,
            'longitude': 139.7004131
        }

        response = c.post('/locations/search', data, **auth_headers)
        print(response.content)
        self.assertEqual(response.status_code, 200)