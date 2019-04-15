#Global variables

MAXCLIENTS = 3
LOGINFILE = "login.txt"

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

loginDictionary = importLogins(LOGINFILE)
