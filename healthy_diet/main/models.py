from django.db import models

class FoodPerDay(models.Model):
    date = models.DateField()
    breakfast = models.CharField('breakfast', max_length=150)
    lunch = models.CharField('lunch', max_length=150)
    dinner = models.CharField('dinner', max_length=150)
    other_food = models.CharField('other food', max_length=150)

    def __str__(self):
        return str((self.data, self.breakfast, self.lunch, self.dinner, self.other_food))
    
    class Meta:
        verbose_name = 'Food in day'
        verbose_name_plural = 'Food in days'