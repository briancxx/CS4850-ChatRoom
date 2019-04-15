import socket

#Global variables

MAXCLIENTS = 3
LOGINFILE = "login.txt"
SERVERPORT = 12492

# Chat Server class

class ChatServer:

    def __init__(self, port):
        self.port = port

        self.s = socket.socket()
        self.s.bind(("", port))
        self.s.listen(MAXCLIENTS)

        while True:
            c, addr = self.s.accept()
            print 'Got connection from', addr
            c.send("Client connected to server")
            c.close()


# Function declarations

def importLogins(loginFile):
    file = open(loginFile, "r")
    for line in file:
        loginInfo = line.split(",")
        loginID = loginInfo[0]
        loginPassword = loginInfo[1]
        loginDictionary = {}
        loginDictionary[loginID] = loginPassword
    file.close()
    return loginDictionary


# Main program

loginDictionary = importLogins(LOGINFILE)

chatServer = ChatServer(SERVERPORT)
