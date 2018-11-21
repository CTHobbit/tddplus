from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from assignmentData.views import home_page  
from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')  

        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Enter Assignment Data</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')  

    def test_uses_home_template(self):
         response = self.client.get('/')
         self.assertTemplateUsed(response, 'home.html') 

    def test_can_save_a_POST_request(self):
         response = self.client.post('/', data={'Assignment ID': '999'})
         self.assertIn('999', response.content.decode()) 
         response = self.client.post('/', data={'Assignment Name': 'Assignment999'})
         self.assertIn('Assignment999', response.content.decode())
         response = self.client.post('/', data={'PEO': 'PEO1'})
         self.assertIn('PEO1', response.content.decode())
         response = self.client.post('/', data={'SO': 'SO1'})
         self.assertIn('SO1', response.content.decode())
         response = self.client.post('/', data={'Class ID': 'CS5513'})
         self.assertIn('CS5513', response.content.decode())
         response = self.client.post('/', data={'Score': '75'})
         self.assertIn('75', response.content.decode())
         response = self.client.post('/', data={'Term': '1'})
         self.assertIn('1', response.content.decode())
         response = self.client.post('/', data={'Year': '2018'})
         self.assertIn('2018', response.content.decode())    