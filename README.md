# FEEDME
Find a food truck, fast!

Try it here!
<url_to_app>

Author: Omar Al-hayderi (https://www.linkedin.com/in/oahayder)

First time using Django (: Shaking the rust off of my beginner Python skills

# Problem & Solution
The problem was to create a service that tells the user what types of food trucks might be found near a specific location on a map. I am primarily a backend engineer, interested in a backend position, so I planned to build an API that returns the nearest food truck(s) from a set of coordinates.

The first step to solving this was understanding the data. With only a weeks exposure to the Data SF API I didn't have time to study it's behaviours which meant I had to make some assumptions:

1. The listings and status of food trucks could change multiple times per week.
2. The API could be unreachable at any time for a prolonged period of time
3. The API could periodically have incorrect data

I tried to solve all these problems by building a daemon process that scrapes the API every night and repopulates a SQL DB that's maintained in this system.

# Tech choices
Python 2.7
Django (https://www.djangoproject.com/)
Django REST framework (http://www.django-rest-framework.org/)
redis-2.10.3 (http://redis.io/)
django-redis-3.8.3 (http://niwibe.github.io/django-redis/)

I have novice experience with Python I got from University. It's been a few years since I used it. I chose to use Python since I know that Uber's backend stack is mostly written in Python. I wanted to show my ability to ramp up quickly.

# Logic, Architecture and Peformance
The tough part of this problem is that we could get requests from users all over the world with trillions of coordinate combinations. This makes the data very hard to cache.

Regardless of client, we can assume there will be a margin of error between the analogous position of the user on earth, and the coordinate set passsed to the API. I used that assumption to attempt to solve the caching problem.

I pictured the earth as a grid with datapoints. I have the grid width and height at 0.0001 degrees. When we get a set of coordinates to query with I round the input to a point on the grid and retreive results. Once the results are cached if we get a request within that same grid element on earth we can return cached data.

