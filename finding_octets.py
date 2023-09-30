import netmiko

ip = ""
last_octet = 1

port = ""
device_type = ""
username = ""
password = ""

def get_ip_int_br(ip):
    net_connect = netmiko.ConnectHandler(
        ip = ip,
        port = port,
        device_type = device_type,
        username = username,
        password = password
    )
    return net_connect.send_command("show ip interface brief")

while last_octet <= 3:
    ip = ip + str(last_octet)
    ip_int_br = get_ip_int_br(ip)
    print(ip_int_br)
    print("-" * 80)
    last_octet +=1
