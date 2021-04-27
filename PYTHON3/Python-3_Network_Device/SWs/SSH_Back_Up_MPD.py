from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from datetime import datetime

with open('Back_Up_List.txt') as f:
    back_up_list = f.read().splitlines()

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

        #COMNADOS FROM BACK-UP FILE
        print('Get Back-Up from ' + device_data['host'])
        config_filename = ('Back-up_' + device_data['host'] + '.txt')  # Important - create unique configuration file name
        for back_up in back_up_list:
            with open("D:\Yerman CR\OneDrive - Axity\BACK-UPs PYTHON\ " + config_filename, 'a') as config_out:
                config_out.write(back_up + '\n')
            Config_Data = net_connect.send_command(back_up)
            with open("D:\Yerman CR\OneDrive - Axity\BACK-UPs PYTHON\ " + config_filename, 'a') as config_out:
                config_out.write(Config_Data + '\n\n')
        print('\n\n******Saved as ' + str(config_filename)+ '\n\n\n')


        net_connect.disconnect()




