from django.db import models
from django.contrib.auth.models import User
from Workout.models import Exercise

# Create your models here.
class OneRepMax(models.Model):
    '''
    The OneRepMax model houses a users one rep max for their selected exercise.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight = models.FloatField()

    def __str__(self):
        '''Returns the string representation of the OneRepMax model'''
        return self.user + ": " + self.exercise + " " + self.weight
