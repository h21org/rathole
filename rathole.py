import paramiko
import time
import concurrent.futures
import logging
import getpass

# Configure logging
logging.basicConfig(filename='ssh_connection.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

MAX_CONNECTIONS = 4
successful_hosts = []

def ssh_connect(host, port, username, password):
    global successful_hosts

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(host, port=port, username=username, password=password, timeout=10)
        logging.info(f"Connected to server {host}.")

        shell = client.invoke_shell()
        shell.send('sudo -i\n')
        time.sleep(1)
        shell.send(f'{password}\n')
        time.sleep(1)

        logging.info(f"Executing script on terminal {host}...")
        script_command = 'bash <(curl -Ls https://raw.githubusercontent.com/Musixal/rathole-tunnel/main/rathole_v2.sh)\n'
        shell.send(script_command)

        # Wait for script execution to finish
        time.sleep(5)
        output = ''
        while shell.recv_ready():
            output += shell.recv(1024).decode('utf-8', errors='ignore')
        logging.info(f"Script output from {host}:\n{output}")

        # Interaction with the script
        responses = ['2\n', '1\n', '2\n']
        for response in responses:
            time.sleep(1)  # Adjust as necessary based on your script's behavior
            shell.send(response)

        # Capture final output
        output = ''
        while shell.recv_ready():
            output += shell.recv(1024).decode('utf-8', errors='ignore')
        logging.info(f"Final output from {host}:\n{output}")

        successful_hosts.append(host)

    except Exception as e:
        logging.error(f"Error connecting to {host}: {e}")
    finally:
        client.close()
        logging.info(f"Connection to {host} closed.")

def connect_to_hosts(hosts, port, username, password):
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_CONNECTIONS) as executor:
        executor.map(lambda host: ssh_connect(host, port, username, password), hosts)

# Get IPs from user input
user_input = input("Please enter the IP addresses separated by commas: ")
hosts = [ip.strip() for ip in user_input.split(',')]

# User input for credentials
port = int(input("Enter SSH port (default 22): ") or 22)
username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

# Connect and execute for each server
while hosts:
    connect_to_hosts(hosts[:MAX_CONNECTIONS], port, username, password)
    hosts = hosts[MAX_CONNECTIONS:]

# Print successful IPs
print("Successfully executed on the following hosts:")
for host in successful_hosts:
    print(host)
