from django.test import TestCase

# Create your tests here.

from .models import *

'''
class ModelsTestCase(TestCase):

    def setUp(self):
        # Instantiate some of my models for testing purposes

        # User, User Profile, Error, Task, StandardReward, User Reward
        username = 'testymctestface'
        password = 'passwordmcpassword'
        email = 'testy@test.com'
        first_name = 'testy'
        last_name = 'mctesterson'
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user_profile = UserProfile(user=user)

    def test_user_name(self):
        user = User.objects.get(username='testymctestface')
        profile = UserProfile.objects.get(user=user)
        self.assertEqual(profile, user.username)

    def test_true(self):
        self.assertTrue(True)
'''
