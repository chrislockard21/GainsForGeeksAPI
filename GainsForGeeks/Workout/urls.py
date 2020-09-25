from django.urls import path, include
from rest_framework import routers
from .views import WorkoutView, UserExerciseView, ExerciseView, GroupView

# Workout URLs
router = routers.DefaultRouter()
router.register('workout', WorkoutView)
router.register('userExercise', UserExerciseView)
router.register('exercise', ExerciseView)
router.register('group', GroupView)


urlpatterns = [
    path('', include(router.urls)),
]
