import json
from threading import Timer
from websocket import create_connection
from django.conf import settings


EVENTS = {
    'refresh': {"action": "refresh", "target": "window", "payload": None}
}


def dispatch(event):
    uri = "ws://{host}:{port}".format(
        host=settings.DJANGO_LIVESYNC['HOST'],
        port=settings.DJANGO_LIVESYNC['PORT'])

    connection = create_connection(uri)
    connection.send(json.dumps(EVENTS[event]))
    connection.close()


def dispatch_async(event):
    Timer(1, dispatch, args=(event,)).start()