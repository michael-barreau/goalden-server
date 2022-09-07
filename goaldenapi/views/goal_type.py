from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from goaldenapi.models import GoalType
from rest_framework import routers
from django.core.exceptions import ValidationError

class GoalTypeView(ViewSet):

    def retrieve(self, request, pk):

        try:    
            goal_type = GoalType.objects.get(pk=pk)
            serializer = GoalTypeSerializer(goal_type)
            return Response(serializer.data)
        except GoalType.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        goal_type = GoalType.objects.all()
        serializer = GoalTypeSerializer(goal_type, many=True)
        return Response(serializer.data) 
    
    def create(self, request):
        goal_type = GoalType.objects.create(
            title=request.data["title"]
        )
        serializer = GoalTypeSerializer(goal_type)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        goal_type = GoalType.objects.get(pk=pk)
        serializer = CreateGoalTypeSerializer(goal_type, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        try:
            goal_type = GoalType.objects.get(pk=pk)
            goal_type.delete()
        except GoalType.DoesNotExist as ex:
            return Response({}, status=status.HTTP_404_NOT_FOUND) 
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    

class GoalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalType
        fields = ('id', 'title')

class CreateGoalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalType
        fields = ['id', 'title']       