from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.cli import CLI

class CustomTopo(Topo):
    def build(self):
        h1 = self.addHost('h1')
        h3 = self.addHost('h3')
        r2 = self.addHost('r2')

        # Add links
        self.addLink(h1, r2)
        self.addLink(h3, r2)

def run():
    topo = CustomTopo()
    net = Mininet(topo=topo, link=TCLink)
    net.start()

    h1, h3, r2 = net.get('h1', 'h3', 'r2')

    # Optional: Add default routes
    h1.cmd('ip route add default via 10.0.1.254')
    h3.cmd('ip route add default via 10.0.2.254')

    CLI(net)
    net.stop()

topos = {'mytopo': (lambda: CustomTopo())}
