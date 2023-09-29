import netmiko

ip = ""
port = ""
device_type = ""
username = ""
password = ""

net_connect = netmiko.ConnectHandler(
    ip = ip,
    port = port,
    device_type = device_type,
    username = username,
    password = password,
)

show_version = net_connect.send_command("show version")
print(show_version)
