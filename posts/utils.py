from .models import Post
from faker import Faker
from random import randint

def create_posts(n=10):
    fake = Faker('pl_PL')
    for _ in range(n):
        created = fake.date_time()
        post = Post(
            title=fake.text(randint(10,30)),
            content=fake.text(randint(100,200)),
            created=created,
            modified=created + fake.time_delta() ,
            published=fake.boolean(),
            spondored=fake.boolean()
                    )
        post.save()