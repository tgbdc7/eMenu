from django.test import TestCase
from .models import MenuCard, Dish
from django.urls import reverse


def create_menu_card(card_name='test_card_name', card_description=""):
    """
    create test object menu card
    :param card_name: str
    :param card_description: str
    :return: object MenuCard
    """
    return MenuCard.objects.create(card_name=card_name, card_description=card_description)


def create_dish(dish_name='test_dish_name', dish_description='', price=9.99,
                make_time=15, is_vege=False, menu_id=(1,)):
    """
    create test dish object
    :param dish_name: str
    :param dish_description: str
    :param price: decimal >0
    :param make_time: int >0
    :param is_vege: boolean
    :param menu_id: tuple of int ManyToManyField
    :return: dish object
    """
    q = Dish.objects.create(dish_name=dish_name, dish_description=dish_description,
                            price=price, make_time=make_time,
                            is_vege=is_vege)
    q.save()
    q.menu_id.set([*menu_id])
    return q


class MenuCardIndexViewTests(TestCase):

    def test_no_card(self):
        """
        If no card exist, an appropriate message is displayed.
        """

        response = self.client.get(reverse('emenu:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No cards menu are available.")
        self.assertQuerysetEqual(response.context['menu_cards_list'], [])

    def test_card_with_no_dish(self):
        """
        Test if card with no dish is displayed in index
        """
        create_menu_card()
        response = self.client.get(reverse('emenu:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['menu_cards_list'], [])
        self.assertContains(response, "No cards menu are available.")

    def test_card_with_one_dish(self):
        """
        Test if card with dish is displayed in index
        """
        create_menu_card()
        create_dish()
        response = self.client.get(reverse('emenu:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['menu_cards_list'], ['<MenuCard: test_card_name>'])

    def test_card_with_one_dish_and_second_card_without_dish(self):
        """
        Test if card with dish is displayed in index and second card without dish is NOT displayed
        """
        create_menu_card()
        create_dish()
        create_menu_card('second_test_card_name')
        response = self.client.get(reverse('emenu:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['menu_cards_list'], ['<MenuCard: test_card_name>'])

    def test_two_cards_with_one_dish(self):
        """
        Test if cards with dishes is displayed in index
        """
        create_menu_card()
        create_menu_card('second_test_card_name')
        create_dish(menu_id=[1, 2])
        response = self.client.get(reverse('emenu:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(list(response.context['menu_cards_list']),
                                 ['<MenuCard: test_card_name>', '<MenuCard: second_test_card_name>'])


class CardDetailViewTests(TestCase):

    def test_card_with_no_dish(self):
        """
        If card with no dish, an appropriate message is displayed.
        """
        c = create_menu_card()
        url = (reverse('emenu:detail_card', args=(c.id,)))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['dishes_list'], [])
        self.assertContains(response, "Card menu are NOT available or card menu hasn't anny dishes.")

    def test_card_with_one_dish(self):
        """
        Test if card detail with one dish is displayed in detail_card page
        """
        c = create_menu_card()
        create_dish()
        url = (reverse('emenu:detail_card', args=(c.id,)))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['dishes_list'], ['<Dish: test_dish_name>'])

    def test_card_with_two_dishes(self):
        """
        Test if card detail with two dishes is displayed in detail_card page
        """
        c = create_menu_card()
        create_dish()
        create_dish(dish_name='second_test_dish_name')
        url = (reverse('emenu:detail_card', args=(c.id,)))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(list(response.context['dishes_list']),
                                 ['<Dish: test_dish_name>', '<Dish: second_test_dish_name>'])


class DishDetailViewTests(TestCase):

    # def test_no_dish(self):
    #     """
    #     Test if dish no exist, an appropriate message is displayed
    #     """
    #     # TODO  test_no_dish
    #     pass
    #
    # def test_dish_without_relationship(self):
    #     """
    #     Test if dish hasn't got relationship with any menu card (menu_id = blank),
    #     an appropriate message is displayed
    #     """
    #     # TODO test_dish_without_relationship
    #     pass

    def test_dish_with_relationship(self):
        """
        Test if dish with relationship with menu card is displayed in dish page
        """
        create_menu_card()
        dish_instance = create_dish()
        url = (reverse('emenu:dish', args=(dish_instance.id,)))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['dish'], dish_instance)
        self.assertEqual(response.context['dish'].dish_name, 'test_dish_name')
