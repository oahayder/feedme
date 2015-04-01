# FEEDME
Find a food truck, fast!

[API Docs](https://arcane-beach-1328.herokuapp.com/proximitysearch/api-docs)

[Closest 10 spots in JSON form? Try it here!](https://arcane-beach-1328.herokuapp.com/proximitysearch/nearby/37.794656/-122.424326?count=10&format=json)

Author: Omar Al-Hayderi (https://www.linkedin.com/in/oahayder)

# Problem & Solution
The problem was to create a service that returns what types of food trucks might be found near a specific location on a map. I am primarily a backend engineer, interested in a backend position, so I planned to build an API that returns the nearest food truck(s) from a set of coordinates with distances.

The first step to solving this was understanding the data. With only one week of exposure to the Data SF API I didn't have time to study it's behaviours which meant I had to make some assumptions:

1. The listings and status of food trucks could change at any given time at an unpredictable rate (Assumed to change on average once per day)
2. The API could be unreachable at any time for a prolonged period of time
3. The API could periodically have incorrect data

I tried to solve all these problems by building a daemon process that scrapes the API every monday and repopulates a SQL DB that's maintained in this system. I use a stateless API to give the FE all the necessary info to display to the user.

# Tech choices
Python 2.7

Django (https://www.djangoproject.com/)

Django REST framework (http://www.django-rest-framework.org/)

PostgreSQL

I have an entry level experience with Python I got from University. It's been a few years since I've used it. I chose to use Python since I know that Uber's backend stack is mostly written in Python and wanted to exhibit my ability to ramp up quickly on new technologies.

This is my first time building a python web app hence my first time using Django and Heroku. From what I've found Django was the most widely used web framework for scalable Python web apps. It has a lot of cool plugins and add ons that make life easy. It also ceoms with an ORM out of the box which cut down on development time which was essential for this one week project.

The Django REST framework was also very useful to out simply output the data in consumable JSON.

# Logic, Architecture and Peformance
The tough part of this problem is that we could get requests from users all over the world with trillions of coordinate combinations. This makes the data very hard to cache. Querying the DB and finding distances to all food trucks is expensive. 

If I had more time, I would like to implement a system to attempt to chache the sorted results. Regardless of client, we can assume there will be a margin of error between the analogous position of the user on earth, and the coordinate set passsed to the API. 

Picture the earth as a grid. The cells have grid width and height of X degrees. When we get a set of coordinates to query with I round the input to a point on the grid and retreive results. Once the results are cached if we get a request within that same grid element on earth we can return cached results and avoid querying the DB and running calculations on every row.

# TODO
* Row cacheing
* Store user data to be used for food truck selection popularity, storing locations and tracking activity
* Track DB activity and site traffic
* Analyze user activity to tweak caching and data population logic
* Develop front end
* Leverage GeoDjango library to globalize app
* Only run the sync_data.pl repopulation script if it has changed, by hashing the source API results and comparing it to a saved value.
* Leverage REDIS for results cacheing.
* Parse schedule file to only return food trucks that are currently open
