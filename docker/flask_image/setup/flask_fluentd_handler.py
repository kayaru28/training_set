

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
        msg =  self.format(record)
        if "HTTP/1" in msg :
            http_log = msg.split(" ")
            http_status = http_log[8]
            request_page = http_log[6]
            request_method = http_log[5]
            if "GET" in request_method:
                request_method = "GET"
            elif "POST" in request_method:
                request_method = "POST"
            
            data = {
                'category': 'http',
                'host': self.hostname,
                'name': record.name,
                'levelname': record.levelname,
                'process': record.process,
                'status': http_status,
                'request_page': request_page,
                'method': request_method,
                'message': msg,
            }
        else:
            data = {
                'category': 'flask',
                'host': self.hostname,
                'name': record.name,
                'levelname': record.levelname,
                'process': record.process,
                'message': msg,
            }
        self.sender.emit(None, data)

    def _close(self):
        self.sender._close()
