from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phoneNumber = models.CharField(max_length=100, default="", blank=True, null=True)
    pic = models.CharField(max_length=10485759, default="", blank=True, null=True)
    NationalID = models.CharField(max_length=100, default="", blank=True, null=True)


class Creditor(models.Model):
    NationalID = models.CharField(max_length=100, default="", blank=True)
    name = models.CharField(max_length=1000, default="", blank=True)
    address = models.CharField(max_length=10000, default="", blank=True)
    phoneNumber = models.CharField(max_length=100, default="", blank=True)
    gender = models.CharField(max_length=100, default="", blank=True)
    additional = models.CharField(max_length=10485759, default="", blank=True, null=True)
    caseNumber = models.CharField(max_length=10000, default="", blank=True, null=True)
    casePlace = models.CharField(max_length=10000, default="", blank=True, null=True)


class Debtor(models.Model):
    NationalID = models.CharField(max_length=100, default="", blank=True, null=True)
    name = models.CharField(max_length=1000, default="", blank=True, null=True)
    address = models.CharField(max_length=10000, default="", blank=True, null=True)
    phoneNumber = models.CharField(max_length=100, default="", blank=True, null=True)
    gender = models.CharField(max_length=100, default="", blank=True, null=True)
    additional = models.CharField(max_length=10485759, default="", blank=True, null=True)
    caseNumber = models.CharField(max_length=10000, default="", blank=True, null=True)
    casePlace = models.CharField(max_length=10000, default="", blank=True, null=True)


