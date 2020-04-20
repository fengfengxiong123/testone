from django.db import models


# Create your models here.
class Rank(models.Model):
    client_num = models.CharField('客户端号', max_length=50)
    score = models.IntegerField('分数')

    def __str__(self):
        return self.client_num
