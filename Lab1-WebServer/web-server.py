from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM) 
#Prepare a sever socket 
serverSocket.bind(('', 6789))
serverSocket.listen(1)
while True:
    print("Ready to serve...")     
    connectionSocket, addr = serverSocket.accept()
    try:
        print("succeed in receiving info...")
        message = connectionSocket.recv(1024)
        print(message)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        header = " HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n" % (len(outputdata))
        connectionSocket.send(header.encode())         
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        header = " HTTP/1.1 404 Found"
        connectionSocket.send(header.encode())
        #Close client socket
        connectionSocket.close()
serverSocket.close()
