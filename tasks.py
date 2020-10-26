from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', broker='pyamqp://guest@localhost//')

app.conf.update(
    timezone='Europe/Paris',
    enable_utc=True,
    beat_schedule = {
        'add-every-10-seconds': {
            'task': 'tasks.add',
            'schedule': 10.0,
            # The issue also works with crontab, but we need to have at least
            # one run before DST change, so with minutely tasks, celery must
            # start 2 minutes before DST change.
            # 'schedule': crontab(minute="*"),
            'args': (16, 16)
        },
    },
)


@app.task
def add(x, y):
    return x + y
