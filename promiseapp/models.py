from django.db import models


# Create your models here.

from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=10, unique=True, null=False)
    election = models.CharField(max_length=10, null=True)
    party = models.CharField(max_length=20, null=True)
    slogan = models.CharField(max_length=20, null=True)
    keyword = models.TextField(null=True)

    def __str__(self):
        return self.name


class Depart(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=False)

    corona = models.CharField(max_length=20, null=True)
    realty = models.CharField(max_length=20, null=True)
    military = models.CharField(max_length=20, null=True)
    politics = models.CharField(max_length=20, null=True)
    economy = models.CharField(max_length=20, null=True)
    construction = models.CharField(max_length=20, null=True)
    environ = models.CharField(max_length=20, null=True)
    science = models.CharField(max_length=20, null=True)
    culture = models.CharField(max_length=20, null=True)
    edu = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.candidate.name


class DepartCon(models.Model):
    depart = models.ForeignKey(Depart, on_delete=models.CASCADE, null=False)

    coronaCon = models.TextField(null=True)
    realtyCon = models.TextField(null=True)
    militaryCon = models.TextField(null=True)
    politicsCon = models.TextField(null=True)
    economyCon = models.TextField(null=True)
    constructionCon = models.TextField(null=True)
    environCon = models.TextField(null=True)
    scienceCon = models.TextField(null=True)
    cultureCon = models.TextField(null=True)
    eduCon = models.TextField(null=True)

    def __str__(self):
        return self.depart.candidate.name