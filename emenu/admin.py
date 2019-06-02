from django.contrib import admin
from .models import MenuCard, Dish


# from .forms import MenuCardModelForm


class DishInline(admin.TabularInline):
    model = Dish.menu_id.through
    extra = 0


# TODO show FilteredSelectMultiple in menu card detail on admin site >>>>/admin/emenu/menucard/2/change/
# TODO show readonly_fields ('create_date', 'update_date') in Menu card admin site change >>>>/admin/emenu/menucard/2/change/
# TODO show readonly_fields ('create_date', 'update_date') in Dishes admin site change >>>>/admin/emenu/menucard/2/change/
# TODO show count dishes  for each cards in Menu Cards list  >>>>/admin/emenu/menucard/


class DishAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Description', {'fields': ['dish_name', 'dish_description', 'price', 'is_vege']}),
        ('Time', {'fields': ['make_time']}),
        ('Menu', {'fields': ['menu_id']}),

    ]

    list_display = ('dish_name', 'price', 'make_time', 'create_date', 'update_date', 'is_vege')
    search_fields = ['dish_name']
    readonly_fields = ('create_date', 'update_date')


class MenuCardAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date', 'update_date',)

    fieldsets = [
        ('Description', {'fields': ['card_name', 'card_description']}),
    ]

    inlines = [DishInline]
    list_display = ('card_name', 'create_date', 'update_date')
    search_fields = ['card_name']

    # for future
    # form = MenuCardModelForm


admin.site.register(Dish, DishAdmin, )
admin.site.register(MenuCard, MenuCardAdmin)
