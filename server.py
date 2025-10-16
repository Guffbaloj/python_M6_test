import threading
import socket
import time

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",55555))
server.listen(2)

clients = []
playerPositions = [[0,4],[39,4]] #första klienten motsvarar possition 1

def handlePlayerInputs(playerInput, playerNr):
    playerInput = playerInput.decode("ascii")
    playerPos = playerPositions[playerNr] #Här ska det tydligen vara lite "risky"
    if playerInput == "s":
        playerPos[1] += 1
    if playerInput == "w":
        playerPos[1] -= 1
    
    


def handleInputs(client):
    while True:
        try:
            playerInput = client.recv(1024)
            handlePlayerInputs(playerInput,clients.index(client))
            
        
        except:
            print("An error has ocurred")
            clients.remove(client)
            client.close()
            break

def sendGamePositions(client):
    while True:
        try:
            allPositions = ""
            for element in playerPositions:
                for n in element:
                    allPositions +=str(n)+";"
            client.send(allPositions.encode("ascii"))
            time.sleep(0.05)
        except:
            print("send failed")
            break

def receive():
    while True:
        #för varje klient som ansluter startas "handel" funktionen i en ny tråd.
        client, addr = server.accept()
        print(f"client has connected from {addr}")
        clients.append(client)

        input_thread = threading.Thread(target = handleInputs,args=(client,))
        input_thread.start()
        position_thread = threading.Thread(target = sendGamePositions,args=(client,))
        position_thread.start()

print("The eye is watching, and the server is listening...")

receive()