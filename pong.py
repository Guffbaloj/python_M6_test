import threading
import time
players = [[0,4],[39,4]]
ball = [20,4]

keyPressed = ""

def updatePositions(keyPressed, playerPositions, ball):
    player1 = playerPositions[0]
    player2 = playerPositions[1]
    if keyPressed == "s":
        player1[1] += 1
    if keyPressed == "w":
        player1[1] -= 1
    
    if keyPressed == "k":
        player2[1] += 1
    if keyPressed == "i":
        player2[1] -= 1

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

def runGame():
    while True:
        global keyPressed
        drawGridd(players, ball)
        updatePositions(keyPressed, players, ball)
        time.sleep(0.3)

def inputManager():
    while True:
        global keyPressed 
        keyPressed = input("")

render_tread = threading.Thread(target = runGame)
render_tread.start()
input_thread = threading.Thread(target = inputManager)
input_thread.start()
