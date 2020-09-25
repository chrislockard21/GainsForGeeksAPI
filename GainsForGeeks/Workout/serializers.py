from rest_framework import serializers
from .models import Workout, UserExercise, Exercise, Group

# Creates the serializers which formats the data to json


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ('__all__')


class UserExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExercise
        fields = ('__all__')


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('__all__')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('__all__')
