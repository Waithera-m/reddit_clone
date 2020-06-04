from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileModelTests(TestCase):
    """
    class facilitates the creation of tests to test profile model's behavior
    """
    def setUp(self):
        """
        method defines the instructions to be executed before each test
        """
        self.user = User(username="Peaches", first_name="may", email="something@something.com", password="somepassword")
        self.user.save()
        self.profile = Profile(bio="some bio", profile_picture="aah.jpg", user=self.user)
    
    def test_instance(self):
        """
        method checks if objects are initialized properly
        """
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        """
        method checks if added profiles are saved to the database
        """
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    
    def test_update_profile(self):
        """
        method checks if a saved profile can be updated
        """
        self.profile.save_profile()
        Profile.objects.filter(pk=self.profile.pk).update(bio="some other bio")
        self.profile.update_profile()
        self.assertEqual(self.profile.bio, 'some other bio')
    
    def test_delete_profile(self):
        """
        function checks if a saved profile object can be deleted
        """
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)
        