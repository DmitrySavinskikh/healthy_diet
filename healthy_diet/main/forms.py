from .models import FoodPerDay
from .models import Sugar
from django.forms import ModelForm, DateInput, TextInput, CheckboxInput


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

class SugarCoutingForm(ModelForm):
    class Meta:
        model = Sugar
        fields = ["date", "sugar"]
        widgets = {
            'date': DateInput(attrs={
                'type': 'date',
                'placeholder': 'Choose date'
            }),
            'sugar': CheckboxInput(attrs={
                'class': 'required checkbox form-control', 
                'placeholder': 'Did you eat sugar today?'
            }),
        }