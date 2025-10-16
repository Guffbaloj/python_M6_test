import threading
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("127.0.0.1",55555))
def processMessage(message):
    numList = message.split(";")
    nums = [int(n) for n in numList if n.isdigit()]
    return [nums[0], nums[1]], [nums[2], nums[3]]

def drawGridd(playerPositions, ballPos):
    print(f"\n"*100 +"===============")
    for y in range(10):
        row = ""
        for x in range(40):
            if [x, y] in playerPositions:
                row += "I"
            
            elif [x, y] == ballPos:
                row += "O"
            else:
                row += " "
        print(row)
    print("=================")
def sendInput():
    while True:
        message = input()
        client.send(message.encode("ascii"))

def recieve():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            pos1, pos2 = processMessage(message)
            drawGridd([pos1, pos2],[4,4])
        except:
            print("something bad has hapend")
            client.close()
            break

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()
input_thread = threading.Thread(target=sendInput)
input_thread.start()