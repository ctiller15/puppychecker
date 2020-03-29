from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
import io

from pupcheck.views import home_page

class HomePageTest(TestCase):
    
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        submitted_data = {}
        submitted_data['file'] = (io.BytesIO(b"abcdef"), 'test.jpg')
        response = self.client.post('/', data=submitted_data)
        
        print(response.content)
        print(submitted_data)
        print(response)
        self.fail("Finish the test!")
