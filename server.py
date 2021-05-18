import socket
import threading

print('Starting...')

port = int(input("What port would you like to use? \n"))


# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', port))
server.listen(5)

print('Server sucessfully created on port ' + str(port))

# Lists For Clients and Their Nicknames
clients = []
nicknames = []
# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)
def broadcastspecial(message,clientnot):
    for client in clients:
        if client != clientnot:
            client.send(message)
# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            
            broadcastspecial(message,client)
            if not message == b'':
                print(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            print('{} left!'.format(nickname))
            nicknames.remove(nickname)
            break
# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        print('before accept')
        client, address = server.accept()
        print('after accept')
        print("Person connected with {}".format(str(address)))
        clients.append(client)
        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        print('Nicks: %s' % nicknames)
        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('\nConnected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
while True:
	receive()
	handle()
