'''
'''
from threading import Lock
from events import *
from logging import getLogger

logger = getLogger(__name__)

class Observable(object):

    def __init__(self):
        self._observers = []
        self._observers_lock = Lock()

    def add_listener(self, callback, mask=EVENT_ALL):
        """
        Adds a listener for scheduler events. When a matching event occurs,
        ``callback`` is executed with the event object as its sole argument.
        If the ``mask`` parameter is not provided, the callback will receive
        events of all types.

        :param callback: any callable that takes one argument
        :param mask: bitmask that indicates which events should be listened to
        """
        self._observers_lock.acquire()
        try:
            self._observers.append((callback, mask))
        finally:
            self._observers_lock.release()

    def remove_listener(self, callback):
        """
        Removes a previously added event listener.
        """
        self._observers_lock.acquire()
        try:
            for i, (cb, _) in enumerate(self._observers):
                if callback == cb:
                    del self._observers[i]
        finally:
            self._observers_lock.release()

    def notify_listeners(self, event):
        self._observers_lock.acquire()
        try:
            observers = tuple(self._observers)
        finally:
            self._observers_lock.release()

        for cb, mask in observers:
            if event.code & mask:
                try:
                    cb(event)
                except:
                    logger.exception('Error notifying listener')
