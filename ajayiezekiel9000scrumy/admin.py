from django.contrib import admin

from .models import ScrumyGoals, ScrumyHistory, GoalStatus

admin.site.register(ScrumyGoals)
admin.site.register(ScrumyHistory)
admin.site.register(GoalStatus)