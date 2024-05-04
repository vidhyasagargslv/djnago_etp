from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class student_details(models.Model):
    name = models.CharField(max_length=100)
    fav_language= models.CharField(max_length=30,
                                    choices=[('python', 'Python'),
                                            ('java', 'Java'),
                                            ('c++', 'C++'),
                                            ('c#', 'C#'),
                                            ('javascript', 'javascript')])
    



class CustomUser (models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    


