from django.urls import path

from apps.cs_gen import views


urlpatterns = [
    path('task/', views.ExerciseView.as_view(), name='exercise-create')
]
