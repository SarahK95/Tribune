import email
from django.test import TestCase
from .models import Editor,Article,tags


# Create your tests here.

class EditorTestClass(TestCase):
    #set up method
    def setUp(self):
        self.james = Editor(first_name = "James", last_name = "Muriuki", email = "james@moringascholl.com")
        
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))    
