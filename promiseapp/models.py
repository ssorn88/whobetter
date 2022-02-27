from django.db import models


# Create your models here.

class Promise(models.Model):
    name = models.CharField(max_length=10, null=True)
    election = models.CharField(max_length=20, null=True)
    party = models.CharField(max_length=20, null=True)
    keyword = models.CharField(max_length=20, null=True)

    corona = models.ForeignKey()
    realty = models.ForeignKey
    military = models.ForeignKey
    politics = models.ForeignKey
    economy = models.ForeignKey
    construction = models.ForeignKey
    environ = models.ForeignKey
    science = models.ForeignKey
    culture = models.ForeignKey
    edu = models.ForeignKey

