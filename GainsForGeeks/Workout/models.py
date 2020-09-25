from django.db import models
from django.contrib.auth.models import User


class Workout(models.Model):
    '''
    The Workout model houses users workouts.
    It acts as a parent to exercises that the user chooses to add later.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_name = models.CharField(max_length=30)
    workout_desc = models.TextField(max_length=300)
    create_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Returns the string representation of the Workout model'''
        return self.workout_name


class Group(models.Model):
    '''
    The Group model houses the different muscle groups and acts as
    a parent to exercises belonging to said muscle group.
    '''
    group_name = models.CharField(max_length=15)

    def __str__(self):
        '''Returns the string representation of the Group model'''
        return self.group_name


class Exercise(models.Model):
    '''
    The Exercise model houses the system level exercises of
    which a user can choose from.
    '''
    muscle_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=50)

    def __str__(self):
        '''Returns the string representation of the Exercise model'''
        return self.exercise_name


class UserExercise(models.Model):
    '''
    The UserExercise model is used to store a copy of the exercise a user
    selects and associate it with the user object and the users workout.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        '''Returns the string representation of the UserExercise model'''
        return '{}: {}'.format(self.user, self.exercise)
