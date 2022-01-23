from .models import Book
from faker import Faker
from random import randint


def create_books(n=2):
    fake = Faker('pl_PL')
    for _ in range(n):
        created = fake.date_time()
        book = Book(
            title=fake.text(randint(10,30)),
            description=fake.text(randint(100,200)),
            available=fake.boolean(),
            publication_year=fake.date_time(),
            created=created,
            modified=created + fake.time_delta(),

                    )
        book.save()

