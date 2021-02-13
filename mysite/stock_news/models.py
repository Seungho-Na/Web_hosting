from django.db import models
from django.utils import timezone
from datetime import datetime

class News(models.Model):
    def __str__(self):
        return self.news_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    news_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    url_text = models.CharField(max_length=200)



