from django.core.management.base import BaseCommand
from parse.models import Details
from parse.workua import main

class Command(BaseCommand):
    help = 'Parsing work.ua'

    def handle(self, *args, **options):
        main()
        pass
        # w = ParseDetails(list)
        # w.save()
