__author__ = 'oahayder'

import urllib2
import json
import os, sys
import django

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "feedme.settings")
django.setup()

from proximitysearch.models import FoodFacility

# We will run this script nightly to update our DB

# Grab JSON via gov API
# TODO get this from conf
response = urllib2.urlopen('https://data.sfgov.org/resource/rqzj-sfat.json')

data = json.load(response)

# TODO Validate data
# TODO If invalid, log and send email to admin

for food_facility in data:

    # Required params
    try:
        # TODO is this correct or is it the coords under location?
        latitude = food_facility['latitude']
        longitude = food_facility['longitude']
        permitId = food_facility['permit']
        name = food_facility['applicant']
        address = food_facility['address']
        status = food_facility['status']
        schedule = food_facility['schedule']
    except KeyError:
        continue

    # Nice to haves
    try:
        fooditems = food_facility['fooditems']
    except KeyError:
        fooditems = ''

    # Update items
    new_facility = FoodFacility(
        permitId = id,
        name = name,
        address = address,
        description = fooditems,
        longitude = longitude,
        latitude = latitude,
        status = status,
        scheduleLink = schedule)

    new_facility.save()



# Remove any entry in the table that wasn't just updated.


