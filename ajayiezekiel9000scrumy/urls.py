from django.urls import path
from . import views


urlpatterns= [
    path('', views.index),
    path('movegoal/<int:goal_id>', views.move_goal, name="movegoal" ),
    path('addgoal/', views.add_goal),
    path('home/', views.home, name='home'),
    ]