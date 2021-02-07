# HealthAI Django chatbot hosted on Heroku

Django Chatbot with the background tasks processing and communications via WebSockets.

## Deployment
You can host it on [Heroku](https://www.heroku.com) for free ([account verification required](https://devcenter.heroku.com/articles/account-verification)).

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Local Development
 - Install new vitural env and install everything `pip install -r requirements.txt`
 - Install [redis-server](https://redis.io/download). For debian based linux: `apt install redis-server`
 - `export DJANGO_SECRET_KEY="somesecretkey"`
 - make sure `DEBUG=True` in settings.py
 - run celery app: `celery -A project worker -l INFO`
 - `python manage.py runserver`

## Technology Stack
 - [Django](https://www.djangoproject.com/) as a main Web Framework
 - [Django Channels](https://github.com/django/channels) as WebSockets framework     
 - [Celery](http://www.celeryproject.org/) as a Asynchronous task queue
 - [Redis](https://redis.io/) as a Message Broker and Cache Backend   
 - [Daphne](https://github.com/django/daphne) as a HTTP and WebSocket protocol server
 - [Heroku](https://www.heroku.com) as a Hosting Platform


## Supported commands
 - `help` - list all available commands

## Credits
[Heroku Chatbot with Celery, WebSockets, and Redis](https://itnext.io/heroku-chatbot-with-celery-websockets-and-redis-340fcd160f06)

