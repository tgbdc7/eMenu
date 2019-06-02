from django import forms
from .models import MenuCard, Dish
from django.contrib.admin.widgets import FilteredSelectMultiple

# TODO Add MenuCardModelForm - show FilteredSelectMultiple in menu card detail on admin site
# class MenuCardModelForm(forms.ModelForm):
#     class Meta:
#         model = MenuCard
#         fields = []
#
#     dishes = forms.ModelMultipleChoiceField(queryset=Dish.objects.all(), required=False,
#                                             widget=FilteredSelectMultiple(verbose_name='Dishes',
#                                                                           is_stacked=False))
#
#     def __init__(self, *args, **kwargs):
#         super(MenuCardModelForm, self).__init__(*args, **kwargs)
#         if self.instance.pk:
#             self.fields['dishes'].initial = self.instance.dishes_set_all()
#
#     def save(self, commit=True):
#         menu_card = super(MenuCardModelForm, self).save(commit=False)
#         if commit:
#             menu_card.save()
#         if menu_card.pk:
#             menu_card.dishes_set = self.cleaned_data['dishes']
#             menu_card.save()
#
#         return menu_card
#
#     def __init__(self, *args, **kwargs):
#         forms.ModelForm.__init__(self, *args, **kwargs)
#         self.fields['dishes'].queryset = Dish.objects.all()
