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

output_list = []
for ip in ip_list:
    net_connect = netmiko.ConnectHandler(
        ip = ip,
        port = port,
        device_type = device_type,
        username = username,
        password = password
    )
    output = net_connect.send_command("show ip interface brief")
    output_list.append(output)

for output in output_list:
    print(output)