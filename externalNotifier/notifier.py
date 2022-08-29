import logging


class Notifier:
    @staticmethod
    def notifier(obj):
        logging.info(f"New notification: {obj}")