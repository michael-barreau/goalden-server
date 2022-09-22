from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from goaldenapi.models import GoalBuddy, Goal, Member
from rest_framework import routers
from django.core.exceptions import ValidationError

class GoalBuddyView(ViewSet):

    def retrieve(self, request, pk):
        try:    
            goal_buddy = GoalBuddy.objects.get(pk=pk)
            serializer = GoalBuddySerializer(goal_buddy)
            return Response(serializer.data)
        except GoalBuddy.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        logged_in_member = Member.objects.get(member=request.auth.user)
        goal_buddies = GoalBuddy.objects.filter(buddy=logged_in_member)
        serializer = GoalBuddySerializer(goal_buddies, many=True)
        return Response(serializer.data) 
    
    def create(self, request):
        goal_buddy = GoalBuddy.objects.create(
            member = Member.objects.get(pk=request.data["member"]),
            goal = Goal.objects.get(pk=request.data["goal"]),
            buddy = Member.objects.get(member=request.auth.user)
             )
        serializer = GoalBuddySerializer(goal_buddy)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def destroy(self, request, pk):
        try:
            goal_buddy = GoalBuddy.objects.get(pk=pk)
            goal_buddy.delete()
        except GoalBuddy.DoesNotExist as ex:
            return Response({}, status=status.HTTP_404_NOT_FOUND) 
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    

class GoalBuddySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalBuddy
        fields = ('id', 'member', 'buddy', 'goal')
        depth = 2

class CreateGoalBuddySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalBuddy
        fields = ['id','member', 'buddy', 'goal']       