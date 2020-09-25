from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Workout, UserExercise, Exercise, Group
from .serializers import WorkoutSerializer, UserExerciseSerializer, ExerciseSerializer, GroupSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class WorkoutView(viewsets.ModelViewSet):
    # Only gets tracks from this year
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        '''Filters for the active user after they are authenticated'''
        qs = super(WorkoutView, self).get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs


class UserExerciseView(viewsets.ModelViewSet):
    # Only gets tracks from this year
    queryset = UserExercise.objects.all()
    serializer_class = UserExerciseSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        '''Filters for the active user after they are authenticated'''
        qs = super(UserExerciseView, self).get_queryset()
        workout = self.request.query_params.get('workout')
        if workout:
            return qs.filter(user=self.request.user, workout=workout)
        else:
            return qs.filter(user=self.request.user)


class ExerciseView(viewsets.ModelViewSet):
    # Only gets tracks from this year
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = (IsAuthenticated,)


class GroupView(viewsets.ModelViewSet):
    # Only gets tracks from this year
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)
