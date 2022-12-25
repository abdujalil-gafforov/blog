from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv
import os

from app1.models import Region


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_name = Region

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='filename for csv file')

    def get_current_app_path(self):
        return apps.get_app_config('app1').path

    def get_csv_file(self, filename):
        app_path = self.get_current_app_path()
        file_path = os.path.join(app_path, "management",
                                 "commands", filename)
        return file_path

    def clear_model(self):
        try:
            self.model_name.objects.all().delete()
        except Exception as e:
            raise CommandError(
                f'Error in clearing {self.model_name}: {str(e)}'
            )

    def insert_currency_to_db(self, data):
        try:
            self.model_name.objects.create(
                name=data["name"]
            )
        except Exception as e:
            raise CommandError(
                f'Error in inserting {self.model_name}: {str(e)}'
            )

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        self.stdout.write(self.style.SUCCESS(f'filename:{filename}'))
        file_path = self.get_csv_file(filename)
        line_count = 0
        try:
            with open(file_path) as csv_file:
                csv_file.readline()
                csv_reader = csv.reader(csv_file)
                self.clear_model()
                for row in csv_reader:
                    _, created = Region.objects.get_or_create(
                        id=row[0],
                        name=row[1],
                    )
            self.stdout.write(
                self.style.SUCCESS(
                    f'{line_count} entries added to Regions'
                )
            )
        except FileNotFoundError:
            raise CommandError(f'File {file_path} does not exist')