#These 4 lines are important
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Project_two.settings')

import django
django.setup()

from user_info.models import User
from faker import Faker

fakegen = Faker()

def add_user(N=5):
    for entry in range(N):
        fake_firstname = fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_email = fakegen.email()
        t=User.objects.get_or_create(First_name=fake_firstname,Last_name=fake_lastname,Email=fake_email)[0]
        t.save()


if __name__=='__main__':
    print('populating scripts')
    add_user(20)
    print('populating scripts')
