from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from goaldenapi.models import GoalBuddy 
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
        goal_buddy = GoalBuddy.objects.all()
        serializer = GoalBuddySerializer(goal_buddy, many=True)
        return Response(serializer.data) 
    
    def create(self, request):
        goal_buddy = GoalBuddy.objects.create(
            title=request.data['member', 'buddy', 'goal']
        )
        serializer = GoalBuddySerializer(goal_buddy)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        goal_buddy = GoalBuddy.objects.get(pk=pk)
        serializer = CreateGoalBuddySerializer(goal_buddy, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

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

class CreateGoalBuddySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalBuddy
        fields = ['id','member', 'buddy', 'goal']       