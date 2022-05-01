from django.shortcuts import render
from .models import Gym, Equipment, Muscle
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404


def workout_homepage(request):
    gyms = Gym.objects.all()
    muscles = Muscle.objects.all()
    return render(request, 'gym/workout_homepage.html', {'gyms':gyms, 'muscles':muscles})

def search(request):
    gyms = Gym.objects.all()
    muscles = Muscle.objects.all()
    if request.method == "POST":
        gym = request.POST.get('gym')
        current_gym = get_object_or_404(Gym, name=gym)
        equipments = Equipment.objects.filter(gym=current_gym)
        current_muscle_name = request.POST.get('muscle')
        current_muscle = get_object_or_404(Muscle, name=current_muscle_name)
        data = []
        for item in current_muscle.equipment.all():
            for item2 in item.gym.all():
                if item2 == current_gym:
                    data.append(item)
        for item in data:
            print(item.name)

        if data:
            return render(request, 'gym/workout_homepage.html', {'data':data, 'gyms':gyms, 'muscles':muscles})
        else:
            return render(request, 'gym/workout_homepage.html', {'error':'No results found.', 'gyms':gyms, 'muscles':muscles})
    return render(request, 'gym/workout_homepage.html', {'gyms':gyms, 'muscles':muscles})