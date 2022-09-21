from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from goaldenapi.models import GoalUser
from rest_framework import routers
from django.core.exceptions import ValidationError

class GoalUserView(ViewSet):

    def retrieve(self, request, pk):

        try:    
            goal_user = GoalUser.objects.get(pk=pk)
            serializer = GoalUserSerializer(goal_user)
            return Response(serializer.data)
        except GoalUser.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        goal_user = GoalUser.objects.all()
        serializer = GoalUserSerializer(goal_user, many=True)
        return Response(serializer.data) 
    
    def create(self, request):
        goal_user = GoalUser.objects.create(
            title=request.data['member', 'goal','check_in_frequency']
        )
        serializer = GoalUserSerializer(goal_user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        goal_user = GoalUser.objects.get(pk=pk)
        serializer = CreateGoalUserSerializer(goal_user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        try:
            goal_user = GoalUser.objects.get(pk=pk)
            goal_user.delete()
        except GoalUser.DoesNotExist as ex:
            return Response({}, status=status.HTTP_404_NOT_FOUND) 
        return Response(None, status=status.HTTP_204_NO_CONTENT)    

class GoalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalUser
        fields = ('id', 'member', 'goal', 'check_in_frequency', 'is_complete')
        depth =1
class CreateGoalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalUser
        fields = ['id','member', 'goal', 'check_in_frequency', 'is_complete']       