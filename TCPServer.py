# Imports
from socket import *
from threading import *
import random

# Server setup
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')
# Client Handler
def handleClient(connectionSocket, address):
    try:

        userInput = connectionSocket.recv(1024).decode()
        print("recieved from client: ", userInput)

        # splits user input up into "parts" so we can define which is the "operation" wanted, and what numbers the user has input
        parts = userInput.split()
    
        operation = parts[0].strip()
        number1 = int(parts[1].strip())
        number2 = int(parts[2].strip())

        # perform operations based on user input
        if operation == "+" :
            result = number1 + number2
        elif operation == "-":
            result = number1 - number2
        elif operation == "random" :
            result = random.uniform(number1, number2)
        
        # if operation isn't found, returns an error message
        else :
            result = "Invalid operation"
        # convert result to string and send it back to the client
        result_str = str(result)
        connectionSocket.send(result_str.encode())

    except Exception as e:
        print("error:", e)
    finally:
        connectionSocket.close()

# Server doing its things..? I think
while True:
    
    connectionSocket, addr = serverSocket.accept()
    Thread(target = handleClient, args=(connectionSocket,addr)).start()
    