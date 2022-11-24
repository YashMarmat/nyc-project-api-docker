import csv
import datetime
from apiapp.customFunctions import modifyDate
from apiapp.models import RideModel
from django.core.management.base import BaseCommand, CommandError
import pytz


class Command(BaseCommand):

    help = 'This command extracts user names from csv and regsiter them in django db, uses Article model.'

    def add_arguments(self, parser):
        parser.add_argument(
            'csv_path', help='requires the csv path, tip: keep the csv in root level.')

    def handle(self, *args, **options):

        self.stdout.write(self.style.SUCCESS(f"Starting up...."))

        required_path = options['csv_path']  # receives csv path

        # extracting data from csv
        with open(required_path) as csv_file:
            data_reader = csv.reader(csv_file, delimiter=',')
            next(data_reader)  # skipping header

            counter = 0
            for each_row in data_reader:
                # print(each_row)

                # dates
                started_at = each_row[2]
                ended_at = each_row[3]

                modified_started_date = modifyDate(started_at)
                modified_ended_date = modifyDate(ended_at)              

                # filling up key value pairs
                ride_id = each_row[0]
                rideable_type = each_row[1]
                start_station_name = each_row[4]
                start_station_id = each_row[5]
                end_station_name = each_row[6]
                end_station_id = each_row[7]
                start_lat = each_row[8] if each_row[8] != "" else 0
                start_lng = each_row[9] if each_row[9] != "" else 0
                end_lat = each_row[10] if each_row[10] != "" else 0
                end_lng = each_row[11] if each_row[11] != "" else 0

                # creating rides
                RideModel.objects.create(
                    ride_id=ride_id,
                    rideable_type=rideable_type,
                    started_at=modified_started_date,
                    ended_at=modified_ended_date,
                    start_station_name=start_station_name,
                    start_station_id=start_station_id,
                    end_station_name=end_station_name,
                    end_station_id=end_station_id,
                    start_lat=start_lat,
                    start_lng=start_lng,
                    end_lat=end_lat,
                    end_lng=end_lng,
                )

                counter += 1

        self.stdout.write(self.style.SUCCESS(
            f"Success, Total objects created: {counter}."))
