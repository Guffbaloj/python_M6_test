import threading
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",5555))
server.listen(2)

clients = []
playerPositions = [[0,0],[0,9]] #första klienten motsvarar possition 1

def broadcast(message):
    for client in clients:
        client.send(message)

def handlePlayerInputs(playerInput, playerNr):
    playerInput = playerInput.decode("ascii")
    playerPos = playerPositions[playerNr]
    
    if playerInput == "s":
        playerPos[1] += 1
    if playerInput == "w":
        playerPos[1] -= 1


def handle(client):
    while True:
        try:
            playerInput = client.recv(1024)
            handlePlayerInputs(playerInput,clients.index(client))
        
        except:
            print("An error has ocurred")
            clients.remove(client)
            client.close()
            break
def send():
    while True:
        allPositions = ""
        for element in playerPositions:
            for n in element:
                allPositions +=str(n)+";"
        
        broadcast(allPositions)

def receive():
    while True:
        #för varje klient som ansluter startas "handel" funktionen i en ny tråd.
        client, addr = server.accept()
        print(f"client has connected from {addr}")
        clients.append(client)
        clientNr = str(clients.index(client))
        client.send(clientNr.encode("ascii"))

        thread = threading.Thread(target = handle,args=(client))
        thread.start()

print("The eye is watching, and the server is listening...")
receive()