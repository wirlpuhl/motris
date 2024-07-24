import keyboard
import os
import time
import random
from copy import deepcopy
from termcolor import colored

class Canvas:
    def __init__(self):
        self._x = 10
        self._y = 20
        self._canvas = [[" " for y in range(self._y)] for x in range(self._x)]

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def setPos(self, pos, mark,):
        self._canvas[pos[0] - 1][pos[1] - 1] = mark

    def print(self):
        self.clear()
        print(f"     LINES - {o.lines:0>3}")
        print(f"  _ _ _ _ _ _ _ _ _ _")
        for y in range(self._y):            
            row = ["|", "|"]
            for x in range(self._x):
                row.insert(-1, self._canvas[x][y])

            if not gameStart:
                if y == 9:
                    row[1:11] = [colored("        ---        ", "white")]
                if y == 10:
                    row[1:11] = [colored("    M O T R I S    ", "white")]
                if y == 11:
                    row[1:11] = [colored("                   ", "light_blue")]
                if y == 12:
                    row[1:11] = [colored(" press S to start  ", "light_blue")]
                if y == 13:
                    row[1:11] = [colored(" press ESC to quit ", "light_grey")]
                if y == 14:
                    row[1:11] = [colored("        ---        ", "white")]
            if y == 0:
                row.append("BEST")
            if y == 1:
                row.append(f"{o.best:0>6}")
            if y == 3:
                row.append("SCORE")
            if y == 4:
                row.append(f"{o.score:0>6}")
            if y == 6:
                row.append("LEVEL")
            if y == 7:
                row.append(f"{o.level:0>2}")
            if y == 9:
                row.append("NEXT")
            if y == 10:
                if o.nextObject[1] == 0:
                    row.append("# #")
                if o.nextObject[1] == 1 or o.nextObject[1] == 3 or o.nextObject[1] == 5:
                    row.append("# # #")
                if o.nextObject[1] == 2:
                    row.append("  # #")
                if o.nextObject[1] == 4:
                    row.append("# #")
                if o.nextObject[1] == 6:
                    row.append("# # # #")
            if y == 11:
                if o.nextObject[1] == 0 or o.nextObject[1] == 2:
                    row.append("# #")
                if o.nextObject[1] == 1:
                    row.append("#")
                if o.nextObject[1] == 3:
                    row.append("  #")
                if o.nextObject[1] == 4:
                    row.append("  # #")
                if o.nextObject[1] == 5:
                    row.append("    #")
            if gameOver:
                if y == 9:
                    row[1:11] = ["       ---         "]
                if y == 10:
                    row[1:11] = [colored("    GAME OVER!     ", "red")]
                if y == 11:
                    row[1:11] = ["                   "]
                if y == 12:
                    row[1:11] = ["press R for restart"]
                if y == 13:
                    row[1:11] = [" press ESC to quit "]
                if y == 14:
                    row[1:11] = ["       ---         "]
            print(" ".join(row))
#Detect Full Row
            if gameStart:
                if  o.movingObject == False and row[1:11] == ["#","#","#","#","#","#","#","#","#","#"]:
                    o.fullRowDetected = True
                    o.fullRows.add(y)
        print("  M M M M M M M M M M")

    def collision(self, pos, object):
        for kor in o.objectList[object]:
            if  (pos[0]+kor[0] <= 0 or pos[0]+kor[0] > self._x or pos[1]+kor[1] < 0 or pos[1]+kor[1] > self._y) or self._canvas[pos[0]+kor[0]-1][pos[1]+kor[1]-1] == "#":
                return True
        else:
            return False
        
    def removeRow(self, rows):
        for x in range(self._x):
            for row in rows:
                self._canvas[x][row] = " "
        self.print()
        time.sleep(0.2)
        for x in range(self._x):
            for row in rows:
                self._canvas[x][row] = "#"
        self.print()
        time.sleep(0.2)
        for x in range(self._x):
            for row in rows:
                self._canvas[x][row] = " "
        self.print()
        time.sleep(0.2)
        for x in range(self._x):
            for row in rows:
                self._canvas[x][row] = "#"
        self.print()
        time.sleep(0.2)
        for x in range(self._x):
            for row in rows:
                del self._canvas[x][row]
                self._canvas[x].insert(0, " ")
#Score/Lines/Level Update
        o.lines = o.lines + len(rows)
        if o.lines >= o.level * 10 + 10:
            o.level = o.level + 1
        if o.speed > 1:
            o.speed = 10 - o.level
        if len(rows) == 1:
            o.score = o.score + 40
        if len(rows) == 2:
            o.score = o.score + 100
        if len(rows) == 3:
            o.score = o.score + 300
        if len(rows) == 4:
            o.score = o.score + 1200
        self.print()
        time.sleep(0.2)
        o.fullRowDetected = False
        o.fullRows = set()

class Objects:
    def __init__(self, canvas):
        self.canvas = canvas
        self.startPos = [5, 2]
        self.pos = []
        self.framerate = 0.05
        self.speed = 10
        self.direction = [0, 0]
        self.activeObject = 0
        self.nextObject = [random.randint(0,6), random.randint(0,6)]
        self.movingObject = False
                                #O                                  #L                                  #Z                                      #T
        self.startObjectList = [[(0, 0), (1, 0), (0, -1), (1, -1)], [(-1, 0), (-1, -1), (0, -1), (1, -1)], [(0, 0), (-1, 0), (0, -1), (1, -1)], [(-1, -1), (0, -1), (1, -1), (0, 0)],
                                [(0, 0), (-1, -1), (0, -1), (1, 0)], [(-1, -1), (0, -1), (1, -1), (1, 0)], [(-2, -1), (-1, -1), (0, -1), (1, -1)]]
                                #iZ                                  #iL                                  #I
        self.objectList = deepcopy(self.startObjectList)
        
        self.fullRowDetected = False
        self.fullRows = set()
        self.score = 0
        self.lines = 0
        self.level = 0
        self.best = 0

    def setObject(self, pos, object, mark):
        for kor in self.objectList[object]:
            self.canvas.setPos([pos[0] + kor[0], pos[1] + kor[1]], mark)

    def down(self):
        return [self.pos[0], self.pos[1] + 1]
    
    def right(self):
        return [self.pos[0] + 1, self.pos[1]]
    
    def left(self):
        return [self.pos[0] - 1, self.pos[1]]
    
    def rotate(self, object):
        testRot = [(0, -1)]
        for kor in self.objectList[object]:
            if kor == (0, 0):
                testRot.append((1, -1))
            if kor == (1, 0):
                testRot.append((1, -2))
            if kor == (1, -1):
                testRot.append((0, -2))
            if kor == (1, -2):
                testRot.append((-1, -2))
            if kor == (0, -2):
                testRot.append((-1, -1))
            if kor == (-1, -2):
                testRot.append((-1, 0))
            if kor == (-1, -1):
                testRot.append((0, 0))
            if kor == (-1, 0):
                testRot.append((1, 0))
#Ausnahme für I
            if kor == (0, -3):
                testRot.append((-2, -1))
            if kor == (-2, -1):
                testRot.append((0, -3))
        return testRot   

    def createNewObject(self): 
        self.objectList = deepcopy(self.startObjectList)
        self.movingObject = True
        self.activeObject = self.nextObject[1]
        del self.nextObject[0]
        self.nextObject.append(random.randint(0,6))
        
stopGame = False
moveRight = False
moveLeft = False
moveDown = False
moveRotate = False
moveDone = True
gameStart = False
gameOver = False

canvas = Canvas()
o = Objects(canvas)
n = 0
k = 0
i = 0
j = 0
while not stopGame:
    with open("highscore.txt", "r") as highscore:
        highscoreList = highscore.readlines()
        for i in range(len(highscoreList)):
            highscoreList[i] = int(highscoreList[i])
        o.best = max(highscoreList)

    if keyboard.is_pressed("s"):       
            gameStart = True 
    while not stopGame and not gameOver and gameStart:
#Keyboard Inputs
        if keyboard.is_pressed("Escape"):       
            stopGame = True 
        if keyboard.is_pressed("d") and moveDone:
            moveRight = True
            moveDone = False
            k = 0
        if keyboard.is_pressed("a") and moveDone:
            moveLeft = True
            moveDone = False
            k = 0
        if keyboard.is_pressed("s") and moveDone:
            moveDown = True
            moveDone = False
            i = 0
        if keyboard.is_pressed("r") and moveDone:
            moveRotate = True
            moveDone = False
            k = 0

        if k == 2:
            moveDone = True
        if k < 2:
            k = k + 1

        if i == 1:
            if o.speed > 1:
                o.speed = 10 - o.level
        if i < 1:
            i = i + 1
#Objekt bewegen
        if moveRight:
            o.setObject(o.pos, o.activeObject, " ")
            if not canvas.collision(o.right(), o.activeObject):
                o.pos = o.right()
                o.setObject(o.pos, o.activeObject, "#")
            else:
                o.setObject(o.pos, o.activeObject, "#")
            moveRight = False

        if moveLeft:
            o.setObject(o.pos, o.activeObject, " ")
            if not canvas.collision(o.left(), o.activeObject):
                o.pos = o.left()
                o.setObject(o.pos, o.activeObject, "#")
            else:
                o.setObject(o.pos, o.activeObject, "#")
            moveLeft = False

        if moveDown:
            n = o.speed
            moveDown = False

        if moveRotate:
            if not o.activeObject == 0:
                lastRotateList = deepcopy(o.objectList)
                o.setObject(o.pos, o.activeObject, " ")
                o.objectList[o.activeObject] = o.rotate(o.activeObject)
                if not canvas.collision(o.pos, o.activeObject):
                    o.setObject(o.pos, o.activeObject, "#")
                else:
                    o.objectList[o.activeObject] = lastRotateList[o.activeObject]
                    o.setObject(o.pos, o.activeObject, "#")
            moveRotate = False

#Neues Objekt generieren
        if o.movingObject == False:
            o.createNewObject()
            o.pos = o.startPos 
            if canvas.collision(o.pos, o.activeObject):
                gameOver = True
                if o.score > o.best:
                    with open("highscore.txt", "a") as highscore:
                        highscore.write(f"\n{o.score}")
                j = 0      
            o.setObject(o.pos, o.activeObject, "#")
            canvas.print()
            n = 0
#Objekt fällt
        if o.movingObject and n == o.speed:
            o.setObject(o.pos, o.activeObject, " ")
            if not canvas.collision(o.down(), o.activeObject):
                o.pos = o.down()
                o.setObject(o.pos, o.activeObject, "#")
            else:
                o.setObject(o.pos, o.activeObject, "#")
                o.movingObject = False   
            n = 0 
        canvas.print()
        if o.fullRowDetected and not o.movingObject:
            canvas.removeRow(o.fullRows)
        time.sleep(o.framerate)
        n = n + 1

    if keyboard.is_pressed("Escape"):       
            stopGame = True    
    if keyboard.is_pressed("r"):       
            gameOver = False
            canvas.__init__()
            o.__init__(canvas)
    if j == 0:
        canvas.print()
        j = 1