from django.db import models
from goaldenapi.models.goal import Goal
from goaldenapi.models.member import Member


class GoalUser(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    check_in_frequency = models.CharField(max_length=55)
    is_complete = models.BooleanField()


