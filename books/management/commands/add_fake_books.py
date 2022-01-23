from django.core.management.base import BaseCommand
from books.utils import create_books


class Command(BaseCommand):
    help='Create fake books'

    def handle(self, *args, **options):
        count = options.get('count')
        create_books(count)
        self.stdout.write('Books has been created')

    def add_arguments(self, parser):
        parser.add_argument(
            '-c',
            '-count',
            type=int,
            default=2,
            dest='count',
            help='Amount of books to generate'
        )
