import json

from django.core.management import BaseCommand, call_command
from django.core.serializers.base import DeserializationError

from users.models import Payments


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        try:
            call_command("loaddata", "payments.json", verbosity=2)
            self.stdout.write(
                self.style.SUCCESS("Данные по платежам успешно загружены.")
            )
        except DeserializationError as e:
            self.stderr.write(self.style.ERROR(f"Ошибка десериализации: {e}"))
