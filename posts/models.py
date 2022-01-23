from django.db import models
from django.contrib.auth.models import User
from common.models import Timestamped


class Post(Timestamped):
    title = models.CharField(verbose_name="Tytuł", max_length=255)
    content = models.TextField(verbose_name="Treść")
    published = models.BooleanField(verbose_name="Opublikowany", default=False)
    spondored = models.BooleanField(verbose_name="Sponsorowany", default=False)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField('tags.Tag', related_name="posts")
    example_file = models.FileField(upload_to='posts/examples/', blank=True, null=True)
    image = models.ImageField(upload_to="posts/images/%Y/%m/%d/", null=True)

    def __str__(self):
        return f"{self.id} {self.title}"




# Create your models here.
