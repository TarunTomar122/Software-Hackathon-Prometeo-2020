from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    verified = models.BooleanField(default=False)
    degree = models.CharField(max_length=150)
    about = models.TextField(max_length=800)
    certificate = models.ImageField(
        upload_to='certificate/',
        default='default.jpg'
    )
    image = models.ImageField(
            upload_to='doctors/',
            default='default.jpg'
        )


class Article(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    image = models.ImageField(
        upload_to='articles/',
        default='default.jpg'
    )
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
