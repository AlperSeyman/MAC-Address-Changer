import subprocess
import argparse
import re


def get_user_input():
    parse_object = argparse.ArgumentParser(description="Change Network Interface and MAC Address")
    parse_object.add_argument("-i","--interface",dest="interface",help="Interface to change",required=True)
    parse_object.add_argument("-m","--mac",dest="mac_address",help="NEW MAC ADRESS!!!",required=True)
    return parse_object.parse_args()

def change_mac_address(user_interface,user_macAddress):
    subprocess.run(["ifconfig", user_interface, "down"])
    subprocess.run(["ifconfig", user_interface, "hw","ether",user_macAddress])
    subprocess.run(["ifconfig", user_interface, "up"])

def control_new_mac(user_interface):
    ifconfig = subprocess.check_output(["ifconfig",user_interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)

    if new_mac: 
        return new_mac.group(0)
    else:
        return None
args = get_user_input()

change_mac_address(args.interface,args.mac_address)

final_mac = control_new_mac(args.interface)

if final_mac == args.interface:
    print("Success!")
else:
    print("Erro!")