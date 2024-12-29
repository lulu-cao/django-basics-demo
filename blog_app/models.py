import datetime
from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
        

class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published")
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)