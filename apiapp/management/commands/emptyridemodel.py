from django.core.management.base import BaseCommand, CommandError
from apiapp.models import RideModel


class Command(BaseCommand):

    help = 'will delete all the objects from Article model.'

    def handle(self, *args, **options):

        number_of_objects = RideModel.objects.all().count()

        if number_of_objects == 0:
            self.stdout.write(self.style.ERROR(f"Model is already empty."))
        else:
            RideModel.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f"Success, Total objects deleted: {number_of_objects}."))
