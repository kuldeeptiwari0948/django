import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)