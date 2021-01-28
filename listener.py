import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # modifying sockets for reusing sockets, 1 to enable
# these options
listener.bind(("10.0.2.15", 4444))
listener.listen(0)  # backlog in the method, 0 backlogs
print("[+] Waiting for incoming connections")
listener.accept()
print("[+] Got a connection")
