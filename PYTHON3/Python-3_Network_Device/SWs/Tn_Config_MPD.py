from netmiko import (ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException,)
from getpass import getpass
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from datetime import datetime

with open('Config_SWs.txt') as f:
    Config_list = f.read().splitlines()

with open('IP_SWs.txt') as f:
    device_list = f.read().splitlines()

for devices in device_list:
        fecha=datetime.now()
        print ('Connecting to device ' + devices + '   ' + str(fecha))
        username= input ('Enter your SSH Username:')
        password=getpass()
        print('Enter your Enable Password')
        enable=getpass()
        device_data = {
            'device_type': 'cisco_ios_telnet',
            'host': devices,
            'username': username,
            'password': password,
            #'port' : 8022, # optional, defaults to 22
            'secret': enable, #'admin2', # optional, defaults to ''
        }

        #ESTABLISH AN SSH CONNECTION AND CHECK IF THERE IS A FAULT
        try:
                net_connect = ConnectHandler(**device_data)
                net_connect.enable()


        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            print(error)
            print('Undefined failed: ' + devices)
            continue

        print(net_connect.find_prompt())

        # COMNADOS FROM CONFIG FILE

        # output = net_connect.send_config_from_file('Config_SWs.txt')  una forma de agregar la configuracion
        output = net_connect.send_config_set(Config_list)
        print(output)
        net_connect.disconnect()
