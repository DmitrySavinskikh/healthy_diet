from .models import FoodPerDay
from django.forms import ModelForm, DateInput, TextInput


class FoodPerDayForm(ModelForm):
    class Meta:
        model = FoodPerDay
        fields = ["date", "breakfast", "lunch", 'dinner', "other_food"]
        widgets = {
            "date": DateInput(attrs={
                'type': 'date',
                'placeholder': 'Choose date'
            }),
            'breakfast': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add your breakfast'
            }),
            'lunch': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add your lunch'
            }),
            'dinner': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add your dinner'
            }),
            'other_food': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Other food'
            }),
        }
