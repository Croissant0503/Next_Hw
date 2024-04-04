from django.db import models

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('취미', '취미'),
        ('음식', '음식'),
        ('프로그래밍', '프로그래밍'),
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='취미')
    post_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title