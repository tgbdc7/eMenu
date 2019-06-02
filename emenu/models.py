from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import Count
from django.db.models import DateTimeField


class MenuCard(models.Model):
    card_name = models.CharField('card name', unique=True, max_length=200)
    card_description = models.TextField('description', null=True)
    create_date = models.DateTimeField('add date', editable=False, auto_now_add=True)
    update_date = models.DateTimeField('update date', editable=False, auto_now=True)

    def __str__(self):
        return self.card_name

    def get_count_dish_in_card(self):
        # TODO return  number - count of dish for card menu
        pass
        # g = self.objects.annotate(num_dish=Count('dish'))
        # result = g['num_dish']



class Dish(models.Model):
    dish_name = models.CharField('name', max_length=200)
    dish_description = models.TextField('description', null=True)
    price = models.DecimalField('price', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    # time in minutes
    make_time = models.IntegerField('make time', validators=[MinValueValidator(1)])
    create_date = models.DateTimeField('create date', auto_now_add=True, editable=False)
    update_date = models.DateTimeField('update date', editable=False, auto_now=True)
    is_vege = models.BooleanField('VEGE')

    # Relationship Fields
    menu_id = models.ManyToManyField(MenuCard, blank=True)

    # TODO add field foto

    def __str__(self):
        return self.dish_name

    # TODO return count of card menu for dish
    # TODO display make time in minutes when < 60
    # TODO display make time in format 1h 30m when > 60
