from django.db import models

class GoalType(models.Model):

    title = models.CharField(max_length=30) 
