import socket


def server_program():
    #get the hostname
    host = socket.gethostname()
    print(host)
    port = (5000) #initiate port no above 1024

    server_socket = socket.socket() # get instance
    #look closely. the bind() function take tuple as argument
    server_socket.bind((host,port)) #bind host address and port together.

    #configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn,address = server_socket.accept() #accept new connection
    print("connection from : " +str(address))
    while True:
        #recive data strem. it won't accept data packets greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            #if data is not received break
            break
        print("from connceted user: "+str(data))
        data = input('->')
        conn.send(data.encode()) #send data to the client

    conn.close() #close the connection

if __name__ == '__main__':
    server_program()
