import socket
import sys
from struct import *
import time

#Convert a string of 6 characters of ethernet address
# into a dash separated hex string
def eth_addr(a):
  b = '%.2x:%.2x:%.2x:%.2x:%.2x:%.2x' % (int(a[0]) , int(a[1]) , int(a[2]), int(a[3]), int(a[4]) , int(a[5]))

  return b

# Create INET, STREAMing socket
try:
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
except Exception as e:
    print('Socket could not be created')
    sys.exit()

# Recibir un paquete
while True:
    #time.sleep(100)
    packet = s.recvfrom(65565)
    # packet string from tuple
    packet = packet[0]
    # parse ethernet header
    eth_lenght = 14
    eth_header = packet[:eth_lenght]
    eth = unpack('!6s6sH', eth_header)
    eth_protocol = socket.ntohs(eth[2])
    print("Destination MAC: " + eth_addr(packet[0:6]) + " Src MAC: "  + eth_addr(packet[6:12]) + ' Protocol: ' + str(eth_protocol))

    # Parse IP packets, IP protocol number = 8
    
    if(eth_protocol == 8):
        # Parse IP header
        # Take first 20 chars for the ip header
        ip_header = packet[eth_lenght:20 + eth_lenght]
        # now unpack them :)
        iph = unpack('!BBHHHBBH4s4s', ip_header)

        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0XF

        iph_lenght = ihl * 4

        ttl = iph[5]
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8])
        d_addr = socket.inet_ntoa(iph[9])
        print("Version: " + str(version) + " IP Header lenght: " + str(ihl) + " TTL: " + str(ttl) + " Protocol: " + str(protocol) + " Source address: " + str(s_addr) + " Destination address: " + str(d_addr))
    
