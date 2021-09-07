import socketserver
import threading
import logging


_LOGGER = logging.getLogger(__name__)

class DraginoTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        _LOGGER.info("{} wrote:".format(self.client_address[0]))
        _LOGGER.info(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

class DraginoTCPServer():
    def __init__(self, host, port):
        """Init."""
        self.host = host
        self.port = port
        self.server = None
        self.start_initiated = False

    """Start the TCP server."""
    def start(self):
        if self.server is None:
            self.start_initiated = True
            def do_start():
                self.server = socketserver.TCPServer((self.host, self.port), DraginoTCPHandler)
                _LOGGER.info("Dragino events TCP server started")
                self.server.serve_forever()
            server_thread = threading.Thread(target = do_start)
            server_thread.start()

    def stop(self):
        """Stop the TCP server."""
        self.start_initiated = False
        if self.server is not None:
            self.server.shutdown()
            self.server.server_close()
            self.server = None
            _LOGGER.info("Dragino events TCP server stopped.")

    def is_start_initiated(self):
        """Return True if a start has recently been initiated."""
        return self.start_initiated

    def is_running(self):
        """Return True if the server is currently running."""
        return self.server is not None

#if __name__ == "__main__":
#    server = DraginoTCPServer("localhost", 9999)
#    server.start()
#    import time
#    time.sleep(5)
#    server.stop()
##    HOST, PORT = "localhost", 9999




    # Create the server, binding to localhost on port 9999
#    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
#        print("Server running...")
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
#        server.serve_forever()
