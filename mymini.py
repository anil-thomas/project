from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myminiNetwork():

    net = Mininet(topo=None,build=False,ipBase='20.0.0.0/8')

    info('Controller added\n')
    controller0=net.addController(name='controller0',
                        controller=RemoteController,
		      	 port=6633)

    info( 'Switches added\n')
    switch1 = net.addSwitch('switch1', cls=OVSKernelSwitch)

    info( 'Hosts added\n')


    host1 = net.addHost('host1', cls=Host, ip='20.0.0.10', defaultRoute=None)
    host2 = net.addHost('host2', cls=Host, ip='20.0.0.20', defaultRoute=None)
    host3 = net.addHost('host3', cls=Host, ip='20.0.0.30', defaultRoute=None)
    host4 = net.addHost('host4', cls=Host, ip='20.0.0.40', defaultRoute=None)
    host5 = net.addHost('host5', cls=Host, ip='20.0.0.50', defaultRoute=None)
    host6 = net.addHost('host6', cls=Host, ip='20.0.0.60', defaultRoute=None)
   

    info( 'Links added\n')
    net.addLink(host1, switch1)
    net.addLink(host2, switch1)
    net.addLink(host3, switch1)
    net.addLink(host4, switch1)
    net.addLink(host5, switch1)
    net.addLink(host6, switch1)

    info( 'Network started\n')
    net.build()
    info( 'Controllers started at 20.0.1.10\n')
    info( '1 OpenFlow switch started\n')
    net.get('switch1').start([controller0])

   
    CLI(net)
    net.stop()

    if __name__ == '__main__':
    setLogLevel( 'info' )
    myminiNetwork()
