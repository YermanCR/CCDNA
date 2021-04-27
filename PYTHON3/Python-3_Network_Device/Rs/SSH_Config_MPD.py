from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from datetime import datetime

with open('IP_Rs.txt') as f:
    device_list= f.read().splitlines()
x=1
for devices in device_list:
        with open('Config_Rs-'+ str(x)+'.txt') as f:
            Config_list = f.read().splitlines()
            x+=1
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

        # COMNADOS FROM CONFIG FILE

        # output = net_connect.send_config_from_file('Config_SWs.txt')  una forma de agregar la configuracion
        output = net_connect.send_config_set(Config_list)
        print(output)
