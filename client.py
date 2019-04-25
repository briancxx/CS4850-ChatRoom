import socket

#Global variables

SERVERPORT = 12492

# Chat Client class

class ChatClient:

    def __init__(self, port):
        self.port = port
        self.s = socket.socket()

    def run(self):
        self.s.connect(("127.0.0.1", self.port))
        print self.s.recv(1024)
        self.s.close()

# Main program

chatClient = ChatClient(SERVERPORT)
chatClient.run()
