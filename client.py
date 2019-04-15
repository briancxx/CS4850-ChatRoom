import socket

#Global variables

SERVERPORT = 12492

# Chat Client class

class ChatClient:

    def __init__(self, port):
        self.port = port

        s = socket.socket()
        s.connect(("127.0.0.1", port))
        print s.recv(1024)
        s.close()

# Main program

chatClient = ChatClient(SERVERPORT)
