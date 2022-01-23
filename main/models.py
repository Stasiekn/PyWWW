from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    bio = models.TextField()

class Post(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} {self.title}"