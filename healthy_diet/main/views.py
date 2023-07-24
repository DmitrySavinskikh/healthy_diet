from django.shortcuts import render, redirect
from datetime import timedelta, datetime
from .models import FoodPerDay, Sugar
from .forms import FoodPerDayForm, SugarCoutingForm


def index(request):
    return render(request, 'main/index.html')

def count_consecutive_days(left_border_date):
    count = 0

    if left_border_date != 0:
        right_border_date = 0
        for item in Sugar.objects.all().order_by('-date'):
            print('item...', item)
            if item.sugar == False:
                right_border_date = item.date
                break
    else:
        return '0 days'

    if right_border_date == 0:
        right_border_date = datetime.now()
    count = right_border_date.date() - left_border_date
    return (str(count).split(', '))[0]

def sugar_counting(request):
    if request.method == 'POST':
        form = SugarCoutingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    form = SugarCoutingForm()
    start_date = 0
    if len(Sugar.objects.all().order_by('-date')) > 0:
        for item in Sugar.objects.all().order_by('date'):
            if item.sugar == True:
                start_date = item.date
                continue 
            else:
                continue

    sugar_free_days = count_consecutive_days(start_date)
    sugar_all_data = Sugar.objects.all().order_by('-date')
    return render(request, 'main/sugar_counting.html', {'form': form, 'sugar_free_days': sugar_free_days, 'sugar_all_data': sugar_all_data})

def all_data(request):
    food_per_day = FoodPerDay.objects.order_by('-date')[:7]
    return render(request, 'main/all_data.html', {'title': 'Main page of this site', 'food_per_day': food_per_day})

def create(request):
    if request.method == 'POST':
        form = FoodPerDayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = FoodPerDayForm()
    dict_add = {
        'form': form
    }
    return render(request, 'main/create.html', dict_add)