from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Interest(models.Model):
    interest_name = models.CharField(max_length=100)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete='')

    def __str__(self):
        return self.interest_name

    def get_absolute_url(self):
        return reverse('my-interest-list')