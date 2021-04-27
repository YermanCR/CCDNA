from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from datetime import datetime

with open('Config_SWs.txt') as f:
    Config_list = f.read().splitlines()

with open('IP_SWs.txt') as f:
    device_list = f.read().splitlines()
ipy=0
ipx=0
for devices in device_list:
        fecha=datetime.now()
        print ('Connecting to device ' + devices + '   ' + str(fecha))
        username= input ('Enter your SSH Username:')
        password=getpass()
        print('Enter your Enable Password')
        enable=getpass()
        device_data = {
            'device_type': 'cisco_ios',
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

        except (AuthenticationException):
            print ('Authentication failure: ' + devices)
            continue
        except (NetMikoTimeoutException):
            print ('Timeout to device: ' + devices)
            continue
        except (EOFError):
            print ('End of file while attempting device ' + devices)
            continue
        except (SSHException):
            print ('SSH Issue. Are you sure SSH is enabled? ' + devices)
            continue
        except Exception as unknown_error:
            print ('Some other error: ' + str(unknown_error))
            continue


        print(net_connect.find_prompt())

        # COMNADOS IN PROGRAM PYTHON

        a=172
        b=16
        x=[100,110,120,130,140,150,160,170,180,190]
        y=[10,20,30,40,50,60,70,80,90,100]
        mask='255.255.255.0'
        vl = [50, 145, 200, 654, 823] #FOR VLAN NO CONTIGUAS WITH 'for vlans in vl:´
        for vlans in range(131, 141): #FOR RANGE VLANs CONTIGUAS
            print("Creating VLANs " + str(vlans))
            config_commands = ['vlan ' + str(vlans),
                               'name VLAN_PY' + str(vlans)]
            output = net_connect.send_config_set(config_commands)
            print(output)
            config_commands = ['interface vlan' + str(vlans),
                               'ip address ' + str(a) + '.' +str (b) + '.' + str (x[ipx]) + '.' + str (y[ipy])+ ' ' + mask,
                               'no shut']
            output = net_connect.send_config_set(config_commands)
            print(output)
            ipx+=1


        ipy+=1
        ipx=0











