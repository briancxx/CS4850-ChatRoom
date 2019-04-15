import socket

#Global variables

MAXCLIENTS = 3
LOGINFILE = "login.txt"
SERVERPORT = 12492

# Chat Server class

class ChatServer:

    def __init__(self, port):
        # Set port
        self.port = port

        # Create socket
        self.s = socket.socket()
        self.s.bind(("", port))
        self.s.listen(MAXCLIENTS)

        # Import logins
        file = open(LOGINFILE, "r")
        for line in file:
            loginInfo = line.split(",")
            loginID = loginInfo[0]
            loginPassword = loginInfo[1]
            self.loginDictionary = {}
            self.loginDictionary[loginID] = loginPassword
        file.close()

        # Start listening
        while True:
            c, addr = self.s.accept()
            print 'Got connection from', addr
            c.send("Client connected to server")
            c.close()

# Main program

chatServer = ChatServer(SERVERPORT)
