# FEEDME
Find a food truck, fast!

[Try it here!](https://arcane-beach-1328.herokuapp.com/proximitysearch/nearby/37.794656/-122.424326?count=10&format=json)

Author: Omar Al-Hayderi (https://www.linkedin.com/in/oahayder)

# Problem & Solution
The problem was to create a service that returns what types of food trucks might be found near a specific location on a map. I am primarily a backend engineer, interested in a backend position, so I planned to build an API that returns the nearest food truck(s) from a set of coordinates.

The first step to solving this was understanding the data. With only one week of exposure to the Data SF API I didn't have time to study it's behaviours which meant I had to make some assumptions:

1. The listings and status of food trucks could change at any given time at an unpredictable rate (Assumed to change on average once per day)
2. The API could be unreachable at any time for a prolonged period of time
3. The API could periodically have incorrect data

I tried to solve all these problems by building a daemon process that scrapes the API every night and repopulates a SQL DB that's maintained in this system.

# Tech choices
Python 2.7

Django (https://www.djangoproject.com/)

Django REST framework (http://www.django-rest-framework.org/)

Gunicorn

PostgreSQL

I have an entry level experience with Python I got from University. It's been a few years since I've used it. I chose to use Python since I know that Uber's backend stack is mostly written in Python and wanted to exhibit my ability to ramp up quickly on a new stack.

This is my first time building a python web app hence my first time using Django.

# Logic, Architecture and Peformance
The tough part of this problem is that we could get requests from users all over the world with trillions of coordinate combinations. This makes the data very hard to cache. Querying the DB and finding distances to all food trucks is expensive. 

If I had more time, I would like to implement a system to attempt to chache the results. Regardless of client, we can assume there will be a margin of error between the analogous position of the user on earth, and the coordinate set passsed to the API. 

Picture the earth as a grid. The cells have grid width and height of X degrees. When we get a set of coordinates to query with I round the input to a point on the grid and retreive results. Once the results are cached if we get a request within that same grid element on earth we can return cached results and avoid querying the DB and running calculations on every row.

# TODO
* Store user data to be used for food truck selection popularity, storing locations and tracking activity
* Track DB activity and site traffic
* Analyze user activity to tweak caching and data population logic
* Develop front end
* Leverage GeoDjango library to globalize app
* Only repopulate data if it has changed, by hashing the source API results and comparing it to a saved value.
