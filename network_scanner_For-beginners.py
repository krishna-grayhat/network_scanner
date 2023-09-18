import scapy.all as scapy
import pyfiglet
text = pyfiglet.figlet_format("NetWork Scanner")
print(text)
print("Youtube = https://www.youtube.com/channel/UCgBKD9xygsy7VRQW7DthTJA ")
print("------------------------------------------------------------------")
print("github = https://github.com/krishna-grayhat ")
print(" ")

user_input = input("Enter The Target IP / IP range = ")
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # its a virtual mac adress it send packet to all
    arp_request_broadcast = broadcast/arp_request
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)  #srp send recive packet
    
    print("IP\t\t\tMAC Address\n-----------------------------------------------------------")
    for element in answered_list:
        print(element[1].psrc +"\t\t" + element[1].hwsrc)

scan(user_input)