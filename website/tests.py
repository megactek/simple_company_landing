from django.test import TestCase

# Create your tests here.

    
class TestPages(TestCase):
    
    def test_home_page(self):
        response =self.client.get('/', follow=True)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_about_page(self):
        response = self.client.get('/about', follow=True)
        self.assertTemplateUsed(response, 'about.html')
    
    def test_services_page(self):
        response =self.client.get('/services', follow=True)
        self.assertTemplateUsed(response, 'services.html')