def main(): 
    # Storing User Input as variables
    webName = input("Enter name of Website: ")
    passLength = int(input("Enter number of characters for your password: "))
    pswd = []
    secret = pswdGenerator(passLength, pswd)

    # Outputs my program's functions
    print(errorMessage(passLength))
    pswdGenerator(passLength, pswd)
    passManager(webName, secret)
    input("Press Enter to exit")
    
def errorMessage(passLength):
    # Generate an error message for the user if passLength < 10 characters
    if passLength < 10:
        return "Error: For better security passwords should be at least 10 characters in length."
    else:
        return "Your password will be generated shortly..."

def pswdGenerator(passLength, pswd):
    # Loops through passLength generating a randomn password
    import random
    secret = ""
    for num in range(1, passLength + 1):
        num = chr(random.randint(ord('!'), ord('~')))
        pswd.append(num)
    for char in pswd:
        secret += char
    return secret

def passManager(webName, secret):
    # Creates a dictionary to store the weName and secret
    myDict = {}
    myDict.update({secret : webName})

    for v in myDict.values():
        webSite = str(v)
    for k in myDict.keys():
        passWord = str(k)
    return print("Your generated password for " + webSite +" is: "+ passWord + "\n")

if __name__ == "__main__":
    main()