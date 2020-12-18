import scapy.all as scapy
import optparse

def user_data():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ipaddress", dest="ip_address", help="ip_address")
    (user_input, argumants) = parse_object.parse_args()
    if not user_input.ip_address:
        print("Please Enter ip address!")
    return user_input




def user_scan(ip):
    arp_packets = scapy.ARP(pdst=ip)
    scapy.ls(scapy.ARP())
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    scapy.ls(scapy.Ether())
    combined_packet = broadcast_packet / arp_packets
    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)
    answered_list.summary()

user_ip_address = user_data()
user_scan(user_ip_address.ip_address)

