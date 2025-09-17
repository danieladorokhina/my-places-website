from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Place
from .forms import PlaceForm
from django.db.models import Sum
import random

def home(request):
    """Головна сторінка з кнопкою "Куди піти сьогодні?"."""
    user = User.objects.first() 
    if request.method == 'POST':
        user_places = Place.objects.filter(user=user)
        total_rating = user_places.aggregate(Sum('rating'))['rating__sum'] or 0

        if total_rating > 0:
            choices = []
            for place in user_places:
                choices.extend([place] * place.rating)

            random_place = random.choice(choices)
            return render(request, 'places/home.html', {'random_place': random_place})

    return render(request, 'places/home.html')

def place_list(request):
    """Сторінка зі списком усіх місць."""
    user = User.objects.first()
    places = Place.objects.filter(user=user)
    return render(request, 'places/place_list.html', {'places': places})

def place_detail(request, place_id):
    """Сторінка з детальним описом одного місця."""
    user = User.objects.first()
    place = get_object_or_404(Place, pk=place_id, user=user)
    return render(request, 'places/place_detail.html', {'place': place})

def add_place(request):    """Сторінка додавання нового місця."""
    user = User.objects.first()
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            new_place = form.save(commit=False)
            new_place.user = user
            new_place.save()
            return redirect('place_list')
    else:
        form = PlaceForm()
    return render(request, 'places/add_place.html', {'form': form})