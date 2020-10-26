# Celery DST change issue

This show a basic example of celery beat DST change issue.

On DST change, celery beat stops sending minutely tasks. This happen on both
DST start or DST end.

## Step to reproduce

(optional) Use virtualenv:

```
mkvirtualenv -p /usr/bin/python3 celery
```

Install celery:

```
pip install celery

# Or using master
pip install git+https://github.com/celery/celery
```

Install faketime, this allow to change time only for one program:
```
sudo apt install faketime
```

Have a RabbitMQ running:

```
docker run -d --name celery-rabbitmq -p 127.0.0.1:5672:5672 rabbitmq:3
```

Run celery beat with faketime (removing celerybeat-schedule file to start from
a clean state):
```
rm celerybeat-schedule

# This is 30 seconds before DST start. The issue will NOT happen.
faketime '2020-03-29 00:59:30Z' celery -A tasks worker --loglevel=INFO -B

# This is 30 seconds before DST end. The issue will happen.
faketime '2020-10-25 00:58:30Z' celery -A tasks worker --loglevel=INFO -B
```