from multiaddr import Multiaddr

from libp2p import Libp2p

l = Libp2p('/tmp/p2pd.sock')
[i, a] = l.identify()

print("Identity: ", i)
print("Multiaddrs: ", a)

ma = Multiaddr(string_addr='/ip4/104.131.131.82/tcp/4001')

l.connect('QmaCpDMGvV2BGHeYERUEnRQAwe3N8SzbUtfsmvsqQLuvuJ', [ma])