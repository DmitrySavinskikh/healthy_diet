from django.shortcuts import render, redirect
from .models import FoodPerDay
from .forms import FoodPerDayForm


def index(request):
    return render(request, 'main/index.html')

def login_system(request):
    return render(request, 'main/login_system.html')

def all_data(request):
    food_per_day = FoodPerDay.objects.order_by('-date')[:7]
    return render(request, 'main/all_data.html', {'title': 'Main page of this site', 'food_per_day': food_per_day})

def create(request):
    if request.method == 'POST':
        form = FoodPerDayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        # else:
        #     error = 'Форма была неверной'

    form = FoodPerDayForm()
    dict_add = {
        'form': form
        # 'error': error
    }
    return render(request, 'main/create.html', dict_add)