# HealthAI Django chatbot hosted on Heroku

Django Chatbot with the background tasks processing and communications via WebSockets.

## Deployment
You can host it on [Heroku](https://www.heroku.com) for free ([account verification required](https://devcenter.heroku.com/articles/account-verification)).

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Local Development
 - Install new vitural env and install everything `pip install -r requirements.txt`
 - Install [redis-server](https://redis.io/download). For debian based linux: `apt install redis-server`
 - `export DJANGO_SECRET_KEY="somesecretkey"`
 - `export REDIS_URL="redis://127.0.0.1:6379/0"`
 - make sure `DEBUG=True` in settings.py
 - run celery app: `celery -A project worker -l INFO`
 - `python manage.py runserver`
 - If you get an nltk error or if the session is closed unexpectedly you may need to download nltk manually
 - run: `import nlkt` and  `nltk.download('punkt')` and `nltk.download('wordnet')`

## Technology Stack
 - [Django](https://www.djangoproject.com/) as a main Web Framework
 - [Django Channels](https://github.com/django/channels) as WebSockets framework     
 - [Celery](http://www.celeryproject.org/) as a Asynchronous task queue
 - [Redis](https://redis.io/) as a Message Broker and Cache Backend   
 - [Daphne](https://github.com/django/daphne) as a HTTP and WebSocket protocol server
 - [Heroku](https://www.heroku.com) as a Hosting Platform
 
## Frontend Android Application
 - Thanks to [Ahmet Özrahat](https://github.com/ahmetozrahat25) for building the front-end android application for the chatbot.
 - You can find the repo [here](https://github.com/ahmetozrahat25/health-ai).


## Supported commands
 - `help` - list all available commands

## Credits
[Heroku Chatbot with Celery, WebSockets, and Redis](https://itnext.io/heroku-chatbot-with-celery-websockets-and-redis-340fcd160f06)

