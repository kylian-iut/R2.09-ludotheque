from django.db import models


# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(blank=True, null=True)
    plateforme = models.ForeignKey('Plateforme', on_delete=models.CASCADE, default=None, null=True, blank=True)
    resume = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length=100, default=None)

    def __str__(self):
        return f"{self.title}, {self.release_date}, {self.resume}, {self.plateforme}, {self.tags}"


class Plateforme(models.Model):
    name = models.CharField(max_length=100)
    creation_date = models.DateField(blank=True, null=True)
    socity = models.CharField(max_length=100,null=True, blank=False)

    def __str__(self):
        return f"{self.name}"
