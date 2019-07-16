# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class UserInfo(models.Model):
    user_type_choices = (
        (1, '普通用户'),
        (2, 'VIP'),
        (3, 'SVIP')
    )
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    user_type = models.IntegerField(choices=user_type_choices)


class UserToken(models.Model):
    user = models.OneToOneField(to='UserInfo')
    token = models.CharField(max_length=64)


class Student(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender_choices = ((1, '男'), (2, '女'))
    gender = models.IntegerField(choices=gender_choices)
    school = models.ForeignKey('School', null=True)


class School(models.Model):
    name = models.CharField(max_length=62)


class Boy(models.Model):
    name = models.CharField(max_length=64)


class Girl(models.Model):
    name = models.CharField(max_length=64)


class Relation(models.Model):
    boy = models.ForeignKey("Boy")
    girl = models.ForeignKey("Girl")


if __name__ == '__main__':
    pass
