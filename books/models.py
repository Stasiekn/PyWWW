from django.db import models
from django.contrib.auth.models import User
from common.models import Timestamped

class Author(Timestamped):
    name = models.CharField(max_length=200)
    birth_year = models.IntegerField()
    death_year = models.IntegerField(blank=True, null=True)
    biogram = models.TextField

    def __str__(self):
        return f"{self.name} ({self.birth_year} - )"


class Book(Timestamped):

    title = models.CharField(max_length=255)
    description = models.TextField()
    available = models.BooleanField(default=False)
    publication_year = models.DateTimeField()
    cover = models.ImageField()
    authors = models.ManyToManyField(Author, related_name="books")
    tags = models.ManyToManyField("tags.Tag", related_name="books")
    cover = models.ImageField(upload_to="books/cover/%Y/%m/%d", blank=True, null=True)

    def __str__(self):
        return f"{self.id} {self.title} available: {self.available}"