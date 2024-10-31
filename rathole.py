import paramiko
import time

def ssh_connect(host, port, username, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(host, port=port, username=username, password=password, timeout=10)
        print(f"Connected to server {host}.")

        shell = client.invoke_shell()
        shell.send('sudo -i\n')
        time.sleep(1)
        shell.send(f'{password}\n')
        time.sleep(1)

        print(f"Executing script on terminal {host}...")

        script_command = 'bash <(curl -Ls https://raw.githubusercontent.com/Musixal/rathole-tunnel/main/rathole_v2.sh)\n'
        shell.send(script_command)
        time.sleep(5)

        output = ''
        while shell.recv_ready():
            output += shell.recv(1024).decode('utf-8')
        print(f"Script output from {host}:\n{output}")

        time.sleep(2)
        shell.send('2\n')
        time.sleep(1)
        shell.send('1\n')
        time.sleep(1)
        shell.send('2\n')
        time.sleep(1)

        output = ''
        while shell.recv_ready():
            output += shell.recv(1024).decode('utf-8')
        print(f"Final output from {host}:\n{output}")

    except Exception as e:
        print(f"Error connecting to {host}: {e}")
    finally:
        client.close()
        print(f"Connection to {host} closed.")

# Get IP addresses from user input
hosts_input = input("Enter the IP addresses separated by commas: ")
hosts = [host.strip() for host in hosts_input.split(',')]
port = 22
username = 'ir'
password = 'ir'

# Connect and execute for each server sequentially
for host in hosts:
    ssh_connect(host, port, username, password)
