from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views import generic
from .models import MenuCard, Dish
from django.db.models import Count


class IndexView(generic.ListView):
    # TODO Pagination
    # paginate_by = 25
    template_name = 'emenu/index.html'
    context_object_name = 'menu_cards_list'

    def get_queryset(self):
        g = MenuCard.objects.annotate(num_dish=Count('dish'))
        return g.filter(num_dish__gte=1).order_by()


class CardDetailView(generic.ListView):
    model = MenuCard
    template_name = 'emenu/detail_card.html'
    context_object_name = 'dishes_list'
    # TODO display card detail = card_name, card_description, create_date, update_date
    title = f"Nazwa KArty {{pk}} "



    def get_queryset(self):
        pk = self.kwargs['pk']

        q = Dish.objects.filter(menu_id=pk)
        # q['card'] = f'Karta nr {pk}'

        return q.order_by()


# TODO displayed message if dish no exist or message hasn't relationship with anny card menu
class DishDetailView(generic.DetailView):
    model = Dish
    template_name = 'emenu/dish.html'
    context_object_name = 'dish'

    def get_queryset(self):
        return Dish.objects.filter(id=self.kwargs['pk'])
