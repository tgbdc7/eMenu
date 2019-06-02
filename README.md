# eMenu
Projekt i implementacja samodzielnego serwisu eMenu, służącego jako restauracyjna karta menu
online.

## Wymagania
- Python 3.7
- django 2.2.1
- coverage #do sprawdzania pokrycia testami


## Instalacja:
- `pip install -r requirements.txt` - instalacja zależności
- `python manage.py makemigrations` - stworzenie tabeli w bazie
- `python manage.py migrate` - zastosowanie zmian w bazie
- `python manage.py createsuperuser` - tworzenie konta admina

## Uruchomienie:
- `python manage.py runserver` - uruchomienie serwera


### Testowanie 
- `python manage.py test emnenu` - uruchomienie testów 
- `coverage run --source='.' manage.py test emenu` - sprawdzanie pokrycie testów 
- `coverage raport -m` - raport pokrycia 


### Testowi użytkownicy:
- TODO