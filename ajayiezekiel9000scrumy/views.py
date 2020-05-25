from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

import random

from .models import GoalStatus, ScrumyGoals, ScrumyHistory


def index(request):
    goal = ScrumyGoals.objects.filter(goal_name="Learn Django")
    return HttpResponse(goal)

def move_goal(request, goal_id):
    dictionary = {"error":"A record with that goal id does not exist"}
    try:
        obj = ScrumyGoals.objects.get(goal_id = goal_id)
    except ObjectDoesNotExist:
        return render(request, 'benpelumiscrumy/exception.html', dictionary)
    else:
        return HttpResponse(obj.goal_name)

def add_goal(request):
    weekly = GoalStatus.objects.get(status_name="Weekly Goal")
    the_user = User.objects.get(username="louis")
    goal_list = ScrumyGoals.objects.all()
    id_dic = {idd.goal_id:idd.goal_name for idd in goal_list}
    number = random.randint(1000,9999)
    if number not in id_dic:
        goal = ScrumyGoals.objects.create(goal_name="Keep Learning Django",
                                    goal_id=number,
                                    created_by="Louis",
                                    moved_by="Louis",
                                    owner="Louis",
                                    goal_status=weekly,
                                    user=the_user
                                )
        return HttpResponse(goal)

def home(request):
    goals = ScrumyGoals.objects.filter(goal_name='Keep Learning Django')
    users = User.objects.all()
    weekly = GoalStatus.objects.get(status_name="Weekly Goal")
    weekly = weekly.scrumy_goal.all()
    daily = GoalStatus.objects.get(status_name="Daily Goal")
    daily = daily.scrumy_goal.all()
    verify = GoalStatus.objects.get(status_name="Verify Goal")
    verify = verify.scrumy_goal.all()
    done = GoalStatus.objects.get(status_name="Done Goal")
    done = done.scrumy_goal.all()
    current_user = request.user
    context = {
        'goals':goals,
        'users':users,
        'weekly':weekly,
        'daily':daily,
        'verify':verify,
        'done':done
        # 'current_user':current_user
    }
    output = ', '.join([goal.goal_name for goal in goals])

    return render(request, "benpelumiscrumy/home.html", context)



