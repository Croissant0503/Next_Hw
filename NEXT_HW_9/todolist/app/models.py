from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    due_date =  models.DateTimeField(null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title
