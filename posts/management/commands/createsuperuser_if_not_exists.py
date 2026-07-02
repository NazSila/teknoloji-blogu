from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create admin user if it does not exist."

    def handle(self, *args, **kwargs):
        User = get_user_model()

        if User.objects.filter(username="admin").exists():
            self.stdout.write(self.style.SUCCESS("Admin already exists."))
            return

        User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="Admin123!"
        )

        self.stdout.write(self.style.SUCCESS("Admin created successfully."))
