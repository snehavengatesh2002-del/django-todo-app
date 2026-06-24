from django.db import models

# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=20)

class completeModel(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=20)


class TrashModel(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=20)
