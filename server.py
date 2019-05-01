# Lab 3 - Chat Room v2
# CS 4850
# Brian Cox
# 01 May 2019

import socket

# Global variables

MAXCLIENTS = 1
LOGINFILE = "users.txt"
SERVERPORT = 12492

# Chat Server class
class ChatServer:

    # Initialize class
    def __init__(self, port):
        # Set port
        self.port = port

        # Create socket
        self.s = socket.socket()
        self.s.bind(("", port))
        self.s.listen(MAXCLIENTS)

        # Import logins
        file = open(LOGINFILE, "r")
        self.loginDictionary = {}
        for line in file:
            if line != "\n":
                loginInfo = line.split(",")
                loginID = loginInfo[0]
                loginPassword = loginInfo[1].rstrip()
                self.loginDictionary[loginID] = loginPassword
        print self.loginDictionary
        file.close()

    # Start running server
    def run(self):
        print("Server running")
        self.connectionDictionary = {}
        # Continuously repeat, waiting for new client
        while True:
            # Accept client
            c, addr = self.s.accept()
            print "Got connection from", addr
            c.send("Welcome to the chat room!")
            self.loginID = ""
            repeat = True
            # Continuously repeat, waiting for input
            while repeat:
                # Receive message from client, break apart message
                message = c.recv(1024)
                print "\"" + message + "\"", "from", addr
                brokeninput = message.split(" ")

                # Try to process input
                try:
                    # LOGOUT REQUEST
                    if brokeninput[0] == "logout":
                        print "LOGOUT REQUEST FROM", addr
                        repeat = False
                        c.close()
                    # LOGIN REQUEST
                    elif brokeninput[0] == "login":
                        print "LOGIN REQUEST FROM", addr
                        # Verify user not logged in already
                        if self.loginID != "":
                            c.send("Server: Cannot switch users while logged in.")
                        # Lookup password, check success
                        elif(self.loginDictionary[str(brokeninput[1])] == brokeninput[2]):
                            print "SUCCESSFUL LOGIN FROM", addr, "TO USER", brokeninput[1]
                            self.loginID = brokeninput[1]
                            c.send("Server: Now logged in to user " + self.loginID + ".")
                        else:
                            print "INVALID LOGIN FROM", addr
                            c.send("Server: Incorrect login.")
                        repeat = True
                    # SEND REQUEST
                    elif brokeninput[0] == "send":
                        if self.loginID != "":
                            c.send(self.loginID + ": " + message[5:])
                        else:
                            c.send("Server: Denied. Please login first.")
                    # NEWUSER REQUEST
                    elif brokeninput[0] == "newuser":
                        # Verify correct number of characters
                        if len(str(brokeninput[1])) < 32 and len(str(brokeninput[2])) <= 8 and len(str(brokeninput[2])) >= 4:
                            # Verify user doesn't already exist
                            if str(brokeninput[1]) not in self.loginDictionary:
                                # Add user to dictionary and to users file
                                self.loginDictionary[str(brokeninput[1])] = brokeninput[2]
                                self.loginID = brokeninput[1]
                                file = open(LOGINFILE, "a")
                                file.write("\n" + brokeninput[1] + "," + brokeninput[2])
                                file.close()
                                c.send("Server: New user created. Now logged in to user " + self.loginID + ".")
                                repeat = True
                            else:
                                c.send("Server: Error. User ID already exists.")
                        else:
                            c.send("Server: User ID must be less than 32 characters, and password must be between 4 and 8.")
                    # UNKNOWN REQUEST
                    else:
                        c.send("Server: Invalid request.")
                        repeat = True
                except:
                    c.send("Server: Invalid request.")

# Main program

chatServer = ChatServer(SERVERPORT)
chatServer.run()
