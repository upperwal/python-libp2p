import varint
import socket
import sys

class Stream:
    def __init__(self, sock):
        self.stream = sock.makefile(mode="b")
        self.sock = sock

    def write(self, msg):
        l = len(msg)
        try:
            self.sock.send(varint.encode(l))
            self.sock.send(msg)
        except Exception as e:
            print(e, sys.stderr)

    def read(self):
        l = varint.decode_stream(self.stream)

        try:
            data = self.stream.read(l)
        except Exception as e:
            print(e, sys.stderr)

        return data