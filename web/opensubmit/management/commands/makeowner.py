from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

from opensubmit.security import make_owner

class Command(BaseCommand):
    help = 'Makes the given user a course owner.'

    def add_arguments(self, parser):
        parser.add_argument('email', nargs=1, type=str)

    def handle(self, *args, **options):
        try:
            u=User.objects.get(email=options['email'][0])
            print("Found %s %s (%s), activating course owner rights."%(u.first_name, u.last_name, u.email))
            make_owner(u)
        except User.DoesNotExist:
            print("This user does not exist.")
