# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Blog(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Street_add = models.TextField()
    Street_add2 = models.TextField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    zip = models.BigIntegerField()
    email = models.CharField(max_length=80)
    areac = models.IntegerField()
    phone = models.BigIntegerField()

    def __str__(self):
        return self.First_name



# Create your models here.
