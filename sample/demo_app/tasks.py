"""Demo Task."""

from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task(name='demo_task')
def demo_task(message):
    result = "Hello %s" % message
    print(result)
    return result
