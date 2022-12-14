from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from goaldenapi.models import Goal, GoalType, Member
from rest_framework import routers
from django.core.exceptions import ValidationError

from goaldenapi.models.goal_user import GoalUser

class GoalView(ViewSet):

    def retrieve(self, request, pk):
        try:    
            goal = Goal.objects.get(pk=pk)
            serializer = GoalSerializer(goal)
            return Response(serializer.data)
        except Goal.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        goals = Goal.objects.all()
        member_id = self.request.query_params.get('member_id', None)
        if member_id is not None:
            goals = goals.filter(created_by_id=member_id)
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data) 

    def create(self, request):
        # created_by= Member.objects.get(member=request.auth.user),
        new_goal = Goal.objects.create(
            created_by= Member.objects.get(member=request.auth.user),
            title=request.data["title"],
            description=request.data["description"],
            type= GoalType.objects.get(pk=request.data["type"]),
        )
        serializer = GoalSerializer(new_goal)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        goal = Goal.objects.get(pk=pk)
        goal.title = request.data["title"]
        goal.description = request.data["description"]
        type= GoalType.objects.get(pk=request.data["type"])
        goal.type = type
        goal.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        try:
            goal = Goal.objects.get(pk=pk)
            goal.delete()
        except Goal.DoesNotExist as ex:
            return Response({}, status=status.HTTP_404_NOT_FOUND) 
        return Response(None, status=status.HTTP_204_NO_CONTENT)           

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('id', 'title', 'description','type','created_by')
        depth = 2     

class CreateGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'title', 'description','type','created_by']   