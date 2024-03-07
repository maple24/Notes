## Reference

[django-and-celery](https://testdriven.io/blog/django-and-celery/)

## why?

Although django handles http requests in multithreads, long-running processes should be run outside the normal HTTP request/response flow, in a background process.

Examples:

- Running machine learning models
- Sending confirmation emails
- Scraping and crawling
- Analyzing data
- Processing images
- Generating reports

## workflow

![workflow](assets/django-celery-flow.png)

## schedule

```python
# schedule a specific time
# Star arguments shortcut to .apply_async. (.delay(*args, **kwargs) calls .apply_async(args, kwargs)).
T.delay(arg, kwarg=value)

T.apply_async((arg,), {'kwarg': value})

# executes in 10 seconds from now.
T.apply_async(countdown=10)

# executes in 10 seconds from now, specified using eta
T.apply_async(eta=now + timedelta(seconds=10))

# executes in one minute from now, but expires after 2 minutes.
T.apply_async(countdown=60, expires=120)

# expires in 2 days, set using datetime.
T.apply_async(expires=now + timedelta(days=2))

# periodic schedule
# in settings.py
CELERY_BEAT_SCHEDULE = {
      'test-every-5-seconds': {
        'task': 'app.tasks.test_celery',
        'schedule': 5.0,
        'args': (),
        'options': {
            'expires': 15.0, #  if it's not able to run this task within 15 seconds, to just cancel it
        },
    },
}
```

## run worker/beat

```sh
# for windows, celery worker has to run with command below
celery -A your-application worker -l info --pool=solo
# or
pip install gevent
celery -A <module> worker -l info -P gevent

# celery beat
celery -A <module> beat -l nfo
```
