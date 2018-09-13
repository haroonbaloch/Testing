import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from apptwo.models import User
from faker import Faker

fakegen = Faker()

#topics = ['Search','Social','Marketplace','News','Games']

#def add_topic():
#    t= Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
#    t.save()
#    return t

def populate(N=5):
    for entry in range(N):

        fake_fname = fakegen.first_name_male()
        fake_lname = fakegen.last_name_male()
        fake_email = fakegen.email()

        usr = User.objects.get_or_create(f_name=fake_fname,l_name=fake_lname,email=fake_email)[0]

    #    acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("populating script")
    populate(20)
    print("populating complte")
