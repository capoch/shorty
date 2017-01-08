from django.core.management.base import BaseCommand, CommandError
from shortener.models import ShortyURL

class Command(BaseCommand):
    help = 'Refreshes all Shortcodes'

    #def add_arguments(self, parser):
    #    parser.add_argument('number', type=int)

    def handle(self, *args, **options):
        print(options)
        return ShortyURL.objects.refresh_shortcodes()
