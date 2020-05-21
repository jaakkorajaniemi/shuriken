from django.db import models
from shuriken.apps.blog.models import Post

# Create your models here.
class Settings(models.Model):
    language = models.CharField(default='en', max_length=2, null=False)
    location = models.CharField(default='jp', max_length=2, null=False)

    # Automatically detect the language of the user (does not save it automatically though)
    def DetectLanguage(self):
        pass

    # Automatically detect the language of the user (does not save it automatically though)
    def DetectLocation(self):
        pass

    # Synchronizes any changes in this object to the session and data layer (if logged in)
    def Update(self):
        pass

class Contact(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)

    # Information about the contacting person
    name = models.CharField(max_length=64, null=False)
    email = models.CharField(max_length=64, null=False)
    company = models.CharField(max_length=64, null=False)

    # Send email receipt of the contact request both to site author and the contactor
    def SendMail(self):
        pass
