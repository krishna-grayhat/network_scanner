import scapy.all as scapy
import argparse
import pyfiglet
text = pyfiglet.figlet_format("NetWork Scanner")
print(text)
print("Youtube = https://www.youtube.com/channel/UCgBKD9xygsy7VRQW7DthTJA ")
print("------------------------------------------------------------------")
print("github = https://github.com/krishna-grayhat ")
print(" ")

def get_arguments():
    parser=argparse.ArgumentParser(description="python script for network scaning",usage="%(prog)s --target 192.168.12.1/24")
    parser.add_argument("-t" , "--target", dest="target", metavar=" ", help="Target IP / IP range.")
    args = parser.parse_args()
    if not args.target:
        parser.error("[+] please spacifie the Target IP / Ip range\n\t\t\t\t( For More Help use -h or --help )")
    return args
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # its a virtual mac adress it send packet to all
    arp_request_broadcast = broadcast/arp_request
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)  #srp send recive packet
    
    print("IP\t\t\tMAC Address\n-----------------------------------------------------------")
    for element in answered_list:
        print(element[1].psrc +"\t\t" + element[1].hwsrc)

args = get_arguments()
scan_result = scan(args.target)
print(scan_result)


# create funtion name scan
# pehla arp te ether da pakit bnaya 
# fir una nu jodta
# fir send karta srp nall te oh do output le k aundi aa answered te unans
#fir loop naal itrate kati
#bus chadiyi aa teri










