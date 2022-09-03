from django.db import models
from goaldenapi.models.goal_user import GoalUser
from goaldenapi.models.goal_type import GoalType

class Goal(models.Model):

    title = models.CharField(max_length=60) 
    description = models.CharField(max_length=100)
    type = models.ForeignKey(GoalType, on_delete=models.CASCADE) 
    created_by = models.ForeignKey(GoalUser, on_delete=models.CASCADE)
