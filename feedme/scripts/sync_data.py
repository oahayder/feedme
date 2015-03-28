__author__ = 'oahayder'

import urllib2
import json
import os, sys
import django

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "feedme.settings")
django.setup()

from proximitysearch.models import FoodFinderInfo

# We will run this script nightly to update our DB

# Grab JSON via gov API
response = urllib2.urlopen('https://data.sfgov.org/resource/rqzj-sfat.json')

data = json.load(response)

# Validate data

# Iterate over JSON elements
for food_facility in data:

    # Required params
    try:
        # TODO is this correct or is it the coords under location?
        latitude = food_facility['latitude']
        longitude = food_facility['longitude']
        permitId = food_facility['permit']
        name = food_facility['applicant']
        address = food_facility['address']
        schedule = food_facility['schedule']
    except KeyError:
        continue

    # Nice to haves
    try:
        fooditems = food_facility['fooditems']
    except KeyError:
        fooditems = ''

    # Update items
    new_facility = FoodFinderInfo(
        permitId = id,
        name = name,
        address = address,
        description = fooditems,
        longitude = longitude,
        latitude = latitude,
        scheduleLink = schedule)

    new_facility.save()



# Remove any entry in the table that wasn't just updated.


