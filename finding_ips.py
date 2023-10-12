import netmiko
import pprint

port = ""
device_type = ""
username = ""
password = ""


ips = (
    "",
    "",
    ""
)

output_list = []

for ip in ips:
    net_connect = netmiko.ConnectHandler(
        ip = ip,
        port = port,
        device_type = device_type,
        username = username,
        password = password
    )
    hostname = net_connect.send_command(
        'sh run | include hostname'
    ).strip()
    ios_xe_version = net_connect.send_command(
        'sh version | section Cisco IOS XE Software, Version'
    ).strip()
    output = (hostname , ios_xe_version)
    output_list.append(output)

pprint.pprint(output_list)