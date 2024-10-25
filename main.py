# main.py
import os
import django

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'theater_lab.settings')

# Initialize Django
django.setup()

# Import your Context class after setting up Django
from context import Context

def call_repository_methods():
    facade = Context()

    # Directors
    print("Directors:")
    directors = facade.directors.get_all()
    for director in directors:
        print(director)  # Виводимо кожного режисера окремо
    print("--------------------------------")
    print(facade.directors.get_by_id(1))  # Отримуємо режисера за ID
    print("--------------------------------")
    print(facade.directors.create("John", "Doe", "1980-01-01"))  # Створюємо нового режисера

    # Theaters
    print("\nTheaters:")
    theaters = facade.theaters.get_all()
    for theater in theaters:
        print(theater)  # Виводимо кожен театр окремо
    print(facade.theaters.get_by_id(1))  # Отримуємо театр за ID
    print(facade.theaters.create("Royal Theater", "123 Main St", 5))  # Створюємо новий театр

    # Actors
    print("\nActors:")
    actors = facade.actors.get_all()
    for actor in actors:
        print(actor)  # Виводимо кожного актора окремо
    print(facade.actors.get_by_id(1))  # Отримуємо актора за ID
    print(facade.actors.create("Jane", "Smith", "1985-05-15"))  # Створюємо нового актора

if __name__ == "__main__":
    call_repository_methods()