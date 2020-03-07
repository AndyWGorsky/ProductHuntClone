from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    pub_date = models.DateField(default=datetime.now())
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='icons/')
    body = models.CharField(max_length=400)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def pub_date_show(self):
        return self.pub_date.strftime('%d %B %Y')

    def summary(self):
        return self.body[:100]
