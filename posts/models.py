from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """
    class facilitates the creation of profile objects
    Args:
        self.bio: profile's bio,
        self.profile_picture: profile's profile image,
        self.user: user associated with the profile,
        self.pub_date: the date that a profile is
    """
    bio = models.CharField(max_length=60)
    profile_picture = models.ImageField(upload_to='profiles/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save_profile(self):
        """
        method saves added profiles to the database
        """
        self.save()
    
    def update_profile(self, using=None, fields=None, **kwargs):
        """
        method updates saved profile object
        """
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)
    
    def delete_profile(self):
        """
        method deletes saved profile object
        """
        self.delete()