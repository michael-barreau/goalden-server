from django.db import models
from goaldenapi.models.goal import Goal
from goaldenapi.models.member import Member

class GoalBuddy(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='%(class)s_member')
    buddy = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='%(class)s_buddy')
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)