from django.shortcuts import render
from .models import FoorPerDay


def index(request):
    return render(request, 'main/index.html')

def login_system(request):
    return render(request, 'main/login_system.html')

def all_data(request):
    food_per_day = FoorPerDay.objects.order_by('-data')[:7]
    return render(request, 'main/all_data.html', {'title': 'Main page of this site', 'food_per_day': food_per_day})