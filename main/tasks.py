from celery import Celery
# from kombu import Exchange, Queue
from kombu.common import Broadcast

BROKER_URL = 'amqp://guest:guest@localhost:5672//'

# celery_exhange = Exchange('q1', type='fanout')
# b = Broadcast(name='q1')


class CeleryConf:
    # List of modules to import when celery starts.
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_IMPORTS = ('main.tasks')
    CELERY_QUEUES = (Broadcast('q1'),)
    CELERY_ROUTES = {
        'tasks.sampletask': {'queue': 'q1'}
    }


celeryapp = Celery('celeryapp', broker=BROKER_URL)
celeryapp.config_from_object(CeleryConf())


@celeryapp.task
def sampletask(form):
    print form
