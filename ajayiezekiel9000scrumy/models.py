from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
        

class GoalStatus(models.Model):
    status_name = models.CharField(max_length = 250)

    class Meta:
        verbose_name_plural = 'GoalStatus'

    def __str__(self):
        return self.status_name
        

class ScrumyGoals(models.Model):
    goal_name =  models.CharField(max_length = 250)
    goal_id = models.IntegerField(default = 1, unique=True)
    created_by = models.CharField(max_length = 50)
    moved_by =  models.CharField(max_length = 50)
    owner =  models.CharField(max_length = 50)
    goal_status = models.ForeignKey(GoalStatus, on_delete = models.PROTECT, related_name='scrumy_goal')
    user = models.ForeignKey(User, related_name='player', on_delete = models.PROTECT)

    class Meta:
        verbose_name_plural = 'ScrumyGoals'

    def __str__(self):
        return self.goal_name


class ScrumyHistory(models.Model):
    moved_by =  models.CharField(max_length = 50)
    created_by =  models.CharField(max_length = 50)
    moved_from =  models.CharField(max_length = 50)
    moved_to =  models.CharField(max_length = 50)
    time_of_action = models.DateTimeField(default = timezone.now)
    goal = models.ForeignKey(ScrumyGoals, on_delete = models.CASCADE, related_name='scrumy_history')

    class Meta:
        verbose_name_plural = 'ScrumyHistories'

    def __str__(self):
        return self.created_by

