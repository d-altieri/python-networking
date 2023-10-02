import netmiko

ip_list = [
    "",
    "",
    ""
]

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

ip_start = ""
last_octet = 1


while last_octet <= 3:
    ip = ip_start + str(last_octet)
    ip_int = get_ip_int_br(ip)
    if len(ip_int) > 0:
        contains_text = True
    if ip in ip_list and contains_text:
        print("IP int from " + ip)
        print(ip_int)
        print("_" * 80)
    last_octet += 1
