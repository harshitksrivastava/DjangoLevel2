import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','trial_project.settings')

import django
django.setup()


# FAKE POP SCRIPT
import random
from trial_urls.models import AccessRecord,Topic,WebPage
from faker import Faker

fakegen = Faker()
topics=['Search','Social','Marketplace','News','Games']

def add_topic():
    #this will return a tuple and we want to grab the first object in tuple which
    #is the reference to model instance thats why [0]is added
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):

        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        WebPg = WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]


        acc_rec = AccessRecord.objects.get_or_create(name=WebPg,date=fake_date)[0]

if __name__=='__main__':
    print("populating script")
    populate(20)
    print("populating complete")
