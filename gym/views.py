from django.shortcuts import render

def workout_homepage(request):
    return render(request, 'gym/workout_homepage.html')
