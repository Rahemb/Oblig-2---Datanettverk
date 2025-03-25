from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

class LinuxRouter(Node):
    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        self.cmd('sysctl -w net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl -w net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()

class CustomTopo(Topo):
    def build(self):
        h1 = self.addHost('h1', ip='10.0.1.1/24')
        h3 = self.addHost('h3', ip='10.0.2.1/24')
        r2 = self.addNode('r2', cls=LinuxRouter, ip='10.0.1.254/24')

        # Links
        self.addLink(h1, r2, intfName2='r2-eth1', params2={'ip': '10.0.1.254/24'})
        self.addLink(h3, r2, intfName2='r2-eth2', params2={'ip': '10.0.2.254/24'})

def run():
    topo = CustomTopo()
    net = Mininet(topo=topo, link=TCLink)
    net.start()

    h1, h3, r2 = net.get('h1', 'h3', 'r2')

    # Set routes
    h1.cmd('ip route add default via 10.0.1.254')
    h3.cmd('ip route add default via 10.0.2.254')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
