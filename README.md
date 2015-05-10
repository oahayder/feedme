# FEEDME
Find a food truck, fast!

[API Docs](https://arcane-beach-1328.herokuapp.com/proximitysearch/api-docs)

[Closest 10 spots in JSON form? Try it here!](https://arcane-beach-1328.herokuapp.com/proximitysearch/nearby/37.794656/-122.424326?count=10&format=json)


# Backend logic
The first step to solving this was understanding the data. With only one week of exposure to the Data SF API I didn't have time to study it's behaviours which meant I had to make some assumptions:

1. The listings and status of food trucks could change at any given time at an unpredictable rate (Assumed to change on average once per day)
2. The API could be unreachable at any time for a prolonged period of time
3. The API could periodically have incorrect data

I tried to solve all these problems by building a daemon process that scrapes the API every monday and repopulates a SQL DB that's maintained in this system.

# Tech
Python 2.7
Django (https://www.djangoproject.com/)
Django REST framework (http://www.django-rest-framework.org/)

PostgreSQL

This is my first web app hence my first time using Django and Heroku. From what I've found Django was the most widely used web framework for scalable Python web apps. It has a lot of cool plugins and add ons that make life easy. It also ceoms with an ORM out of the box which cut down on development time which was essential for this one week project.

The Django REST framework was also very useful to out simply output the data in consumable JSON.

Author: Omar Al-Hayderi (https://www.linkedin.com/in/oahayder)
