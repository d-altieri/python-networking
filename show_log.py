import netmiko

csr1 = ""
csr2 = ""
csr3 = ""


port = ""
device_type = ""
username = ""
password = ""

def get_log(ip):
    net_connect = netmiko.ConnectHandler(
        ip = ip,
        port = port,
        device_type = device_type,
        username = username,
        password = password
    )
    return net_connect.send_command("show log")

csr1_log = get_log(csr1)
csr2_log = get_log(csr2)
csr3_log = get_log(csr3)

print(csr1_log)
print(csr2_log)
print(csr3_log)
