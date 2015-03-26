import urllib2
import json
from facility.models import FacilityInfo

__author__ = 'oahayder'

# We will run this script nightly to update our DB

# Grab JSON via gov API
response = urllib2.urlopen('https://data.sfgov.org/resource/rqzj-sfat.json')

data = json.load(response)

# Validate data

# Iterate over JSON elements
for food_facility in data:
    id = food_facility['permit']
    name = food_facility['applicant']
    address = food_facility['address']
    fooditems = food_facility['fooditems']
    schedule = food_facility['schedule']
    latitude = food_facility['location']['latitude']
    longitude = food_facility['location']['longitude']

    # Update items with same permit in DB
    new_facility = FacilityInfo(
        id = id,
        name = name,
        address = address,
        description = fooditems,
        longitude = longitude,
        latitude = latitude,
        scheduleLink = schedule)

    new_facility.save()



# Remove any entry in the table that wasn't just updated.


