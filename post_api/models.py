from django.db import models
from django.contrib.auth.models import User

from city_api.models import Borough

class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    borough_code = models.ForeignKey(Borough, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title