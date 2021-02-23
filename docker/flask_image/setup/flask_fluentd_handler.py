

from logging import Handler
import socket
from fluent import sender

class FlaskFluentHandler(Handler):
    def __init__(
            self, tag, host='localhost', port=24220, timeout=3.0,
            verbose=False):
        Handler.__init__(self)
        self.tag = tag
        self.sender = sender.FluentSender(tag,
                                          host=host, port=port,
                                          timeout=timeout, verbose=verbose)
        self.hostname = socket.gethostname()

    def emit(self, record):
        if record.levelno < self.level:
            return
        msg = self.format(record)
        data = {
            'host': self.hostname,
            'name': record.name,
            'levelname': record.levelname,
            'process': record.process,
            'message': msg,
        }
        self.sender.emit(None, data)

    def _close(self):
        self.sender._close()
