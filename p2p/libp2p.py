import socket
import sys
import p2pd_pb2
import base58
from multiaddr import Multiaddr
from stream import Stream

class Libp2p:
    def __init__(self, socketPath):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        try:
            self.sock.connect(socketPath)
            self.stream = Stream(self.sock)
        except socket.error as msg:
            print(msg, sys.stderr)
            sys.exit(1)
    
    def identify(self):
        req = p2pd_pb2.Request()
        req.type = p2pd_pb2.Request.IDENTIFY
        
        bb = req.SerializeToString()
        
        self.stream.write(bb)
        data = self.stream.read()

        res = p2pd_pb2.Response()
        res.ParseFromString(data)
        
        id = base58.b58encode(res.identify.id)

        addrs = []
        for add in res.identify.addrs:
            ma = Multiaddr(bytes_addr=add.hex())
            addrs.append(ma)

        return [id, addrs]
    
    def connect(self, peerId, addrs):

        req = p2pd_pb2.Request()
        for addr in addrs:
            req.connect.addrs.append(addr.to_bytes())
        req.connect.peer = base58.b58decode(peerId)
        req.type = p2pd_pb2.Request.CONNECT

        outbound = req.SerializeToString()
        self.stream.write(outbound)

        inbound = self.stream.read()
        res = p2pd_pb2.Response()
        res.ParseFromString(inbound)

        print(res)

