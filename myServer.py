#Create a local host server
import socket
HOST="localhost"
PORT=5000
BUFSIZE=1024
ADDRESS=(HOST,PORT)
server = socket.socket()
server.bind(ADDRESS)
server.listen(1)

while True:
    #Send a welcome message with current date & time.
    print("Waiting for connection...")
    (client,address)=server.accept()
    print("...Connection from ",ADDRESS)
    client.send("You are now connected to PassGen!".encode())

#Inner loop to open a chat function with a Client
    while True:
        def main(): 
            # Storing Client Input as variables
            client.send(bytes("Enter a website name or Press 'q' to quit: ".encode()))
            webName = (client.recv(BUFSIZE)).decode()

            if webName != 'q':
                client.send(bytes("Enter number of characters for your password: ".encode()))
                passLength = (client.recv(BUFSIZE)).decode()
                passLength = int(passLength)
                pswd = []
                secret = pswdGenerator(passLength, pswd)
                
                # Function calls
                errorMessage(passLength)
                pswdGenerator(passLength, pswd)
                passManager(webName, secret)
            elif webName == 'q':
                client.close()
            
        def errorMessage(passLength):
            # Generate an error message for the user if passLength < 10 characters
            if passLength < 10:
                return client.send(bytes("Error: For better security passwords should be at least 10 characters in length.".encode()))
            else:
                return client.send(bytes("Your password will be generated shortly...\nPress 'Enter' to continue...".encode()))

        def pswdGenerator(passLength, pswd):
            # Loops through passLength generating a randomn password
            import random
            secret = ""
            for num in range(1, passLength + 1):
                num = chr(random.randint(ord('!'), ord('~')))
                pswd.append(num)
            for char in pswd:
                secret += str(char)
            return secret

        def passManager(webName, secret):
            myDict = {}
            myDict.update({secret : webName})

            for v in myDict.values():
                webSite = str(v)
            for k in myDict.keys():
                passWord = str(k)
            complete = str("Your generated password for " + webSite +" is: "+ passWord + "\n")
            return client.send(bytes(complete.encode()))

        if __name__ == "__main__":
            main()