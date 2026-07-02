from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Admin kullanıcısı yoksa oluşturur."

    def handle(self, *args, **options):
        User = get_user_model()

        if User.objects.filter(username="admin").exists():
            self.stdout.write(self.style.SUCCESS("Admin kullanıcısı zaten var."))
            return

        User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="Admin123!"
        )

        self.stdout.write(self.style.SUCCESS("Admin kullanıcısı oluşturuldu."))
