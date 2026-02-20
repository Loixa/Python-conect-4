import os
import time
class ConectFour:
            currentGame = {}
            turn = 1
            winner = False
            def __init__(self, player1="player1", player2="player2"):
                self.player1=player1
                self.player2=player2
            def printNames(self):
                print("*********** "+self.player1+" vs "+self.player2+" ************")
            
            def gameBoard(self):
               
               topLine =["***************************************"]
               lineA = ["   A **| "," "," | "," "," | "," "," | "," "," | "," "," | "," "," | "," "," |***"]
               lineB = ["   B **| "," "," | "," "," | "," "," | "," "," | "," "," | "," "," | "," "," |***"]
               lineC = ["   C **| "," "," | "," "," | "," "," | "," "," | "," "," | "," "," | "," "," |***"]
               lineD = ["   D **| "," "," | "," "," | "," "," | "," "," | "," "," | "," "," | "," "," |***"]
               lineE = ["   E **| "," "," | "," "," | "," "," | "," "," | "," "," | "," "," | "," "," |***"]
               lineF = ["   F **| "," "," | "," "," | "," "," | "," "," | "," "," | "," "," | "," "," |***"]
               lineG = ["   G **| "," "," | "," "," | "," "," | "," "," | "," "," | "," "," | "," "," |***"]
               bottomLine = ["""***************************************
******** 1 | 2 | 3 | 4 | 5 | 6 | 7 |***
 ---------------------------------------"""]
        
        
               boardlist={"top":topLine,"A": lineA,"B":lineB, "C":lineC,"D":lineD,"E":lineE,"F":lineF,"G":lineG,"bottom":bottomLine}
        
               
        
               self.currentGame = boardlist
               
            def playChip(self,chip,positionNum):
                positionLetter = ""
                position = []
                
                nc = 0
                if positionNum == "1":
                       nc = 1
                elif positionNum == "2":
                       nc = 3
                elif positionNum == "3":
                       nc = 5
                elif positionNum == "4":
                       nc = 7
                elif positionNum == "5":
                       nc = 9
                elif positionNum == "6":
                       nc = 11
                elif positionNum == "7":
                       nc = 13
                positionLetter = self.checkBoard(positionNum)
                position = self.currentGame[positionLetter]
                position[nc] = chip
                self.currentGame[positionLetter] = position
                #check for winner
                self.checkWinner(nc,positionLetter,chip)
                
                if positionNum == "1":
                    self.checkBoard("1")
                #position = self.currentGame[positionLetter]
        
        
                #if int(positionNum) % 2 ==0 and int(positionNum)>0 or int(positionNum)==1:
                 #   position[int(positionNum)] = chip
                    
                
                #self.currentGame[positionLetter] = position
            
            def checkBoard(self, num):
                letter = ""
                checking = False
                check = []
                nc = 0
                if num == "1":
                    nc = 1
                elif num == "2":
                    nc = 3
                elif num == "3":
                    nc = 5
                elif num == "4":
                    nc = 7
                elif num == "5":
                    nc = 9
                elif num == "6":
                    nc = 11
                elif num == "7":
                    nc = 13
                    
                while checking == False:
                    check = self.currentGame["G"]
                    if check[nc] == " ":
                        letter = "G"
                        break
                    check = self.currentGame["F"]
                    if check[nc] == " ":
                        letter = "F"
                        break
                    check = self.currentGame["E"]
                    if check[nc] == " ":
                        letter = "E"
                        break
                    check = self.currentGame["D"]
                    if check[nc] == " ":
                        letter = "D"
                        break
                    check = self.currentGame["C"]
                    if check[nc] == " ":
                         letter = "C"
                         break
                    check = self.currentGame["B"] 
                    if check[nc] == " ":
                         letter = "B"
                         break
                    check = self.currentGame["A"]
                    if check[nc] == " ":
                        letter = "A"
                        break
                    else:
                        print("ERROR")
                        break
                
                return letter
            
            
            
            def updateBoard(self):
                for value in self.currentGame.values():
                    print(*value,sep="")
        
            def clearBoard(self):
              print('\n' * 30)
            
            def playerInput(self, playerIn):
                    while True:
                        play = input(playerIn + " choose a number to play:")
                        if int(play) > 0 and int(play) < 8:
                            break
                        else:
                            print("Please enter a valid input!")
                    return play
            
            def playgame(self):
                play=""
                if self.turn == 1:
                    play = self.playerInput(self.player1)
                    self.playChip("X",play)
                    self.turn = 2
                elif self.turn == 2:
                    play = self.playerInput(self.player2)
                    self.playChip("O", play)
                    self.turn = 1
                
        
            def playerNames(self):
                self.player1 = input("Player 1 Enter Name: ")
                self.player2 = input("Player 2 Enter Name: ")
            
            def changePosition(self,position,direction):
                poschange = ""
            #move up
                if direction == "UP":
                    if position == "G":
                        poschange = "F"
                    elif position == "F":
                        poschange = "E"
                    elif position == "E":
                        poschange = "D"
                    elif position == "D":
                        poschange = "C"            
                    elif position == "C":
                        poschange = "B"
                    elif position == "B":
                        poschange = "A"
                    elif position == "A":
                        print("out of bound up")
                        poschange = "out of bound"
            #MOVE DOWN POSITION
                elif direction == "DOWN":
                     if position == "G":
                         poschange = "out of bound"
                         print("out of bound down")
                     elif position == "F":
                         poschange = "G"
                     elif position == "E":
                         poschange = "F"
                     elif position == "D":
                         poschange = "E"            
                     elif position == "C":
                         poschange = "D"
                     elif position == "B":
                         poschange = "C"
                     elif position == "A":
                         poschange = "B"
            #CROSS RIGHT position
             #   elif direction == "CROSS RIGHT":
            #        if position == "G":
                        #poschange ="F"
                        
                return poschange
                
                
                
            
            def checkWinner(self, pnum,plett,chip):
                con4 = 1
                line = []
                pnumtest = pnum
                playername = ""
                line = self.currentGame[plett]
                if chip == "X":
                    playername = self.player1
                elif chip == "O":
                    playername = self.player2
                
                
                #check horizontal right**********************************************
                while True:
                    if pnum + 2 < 15 and  line[pnum + 2] == chip:      
                        con4 += 1
                        pnum += 2
                        
                        if con4 >= 4:
                            break
                        
                    else:
                        
                        break
                pnum = pnumtest
                #check horizontal left**********************************************
                while True:
                    if pnum + 2 < 15 and pnum - 2 > 0 and line[pnum - 2] == chip:
                        con4 += 1
                        pnum -= 2
                        if con4 >= 4:
                            break
                    else:
                        break
                #check vertical up**********************************************
                #left and right is no go so reset and check up and down
                con4 = 1
                pnum = pnumtest
                while True:
                    newposition = self.changePosition(plett,"UP")
                    if newposition == "out of bound":
                        break

                    line = self.currentGame[newposition]
                    
                    if line[pnum] == chip:
                        con4 += 1
                        
                    else:
                        
                        break
                #check down*****************************************************
                con4 = 1
                pnum = pnumtest
                downpost = plett
                while True:
                    newposition = self.changePosition(downpost,"DOWN")
                    if newposition == "out of bound":
                        break
                    line = self.currentGame[newposition]
                    
                    if line[pnum] == chip:
                        con4 += 1
                        downpost = newposition
                    
                    else:
                    
                        break
                #check cross ***********************************************
                con4 = 1
                crosspost = plett
                pnum = pnumtest
                while True:
                    newposition = self.changePosition(crosspost,"UP")
                    if newposition == "out of bound":
                        break
                    line = self.currentGame[newposition]
                    if pnum + 2 < 15 and line[pnum + 2] == chip:
                        con4 += 1
                        pnum += 2
                        crosspost = newposition
                    else:
                        
                        break
                pnum=pnumtest
                crosspost = plett
                pnum = pnumtest
                if con4 != 4:
                    while True:
                        newposition = self.changePosition(crosspost,"DOWN")
                        if newposition == "out of bound":
                            break
                        line = self.currentGame[newposition]
                        if pnum + 2 < 15 and pnum - 2  > 0 and line[pnum - 2] == chip:
                            con4 += 1
                            pnum -= 2
                            crosspost = newposition
                        else:
                            break
            #check cross up left right down*******************************************
                con4 = 1
                crosspost = plett
                pnum = pnumtest         
                while True:
                    newposition = self.changePosition(crosspost,"UP")
                    if newposition == "out of bound":
                        break
                    line = self.currentGame[newposition]
                    if pnum + 2 < 15 and pnum - 2 > 0 and line[pnum -2 ] == chip:
                        con4 += 1
                        pnum -= 2
                        crosspost = newposition
                        print("found one up left")
                    else:
                        print("break")              
                        break
                    pnum=pnumtest
                    crosspost = plett
                    pnum = pnumtest
                if con4 != 4:
                    while True:
                        newposition = self.changePosition(crosspost,"DOWN")
                        if newposition == "out of bound":
                            break
                        line = self.currentGame[newposition]
                        if pnum + 2 < 15 and line[pnum + 2] == chip:
                            con4 += 1
                            pnum += 2
                            print("found one down right")
                            crosspost = newposition
                        else:
                            print("break 2")
                            break
            #check if theres 4 in a row **********************************************
                if con4 == 4:
                    
                    self.winner = True
                    self.updateBoard()
                    print(playername + " WINS!!!!!!!!!!!!!!!!!")
            
            
            
            
            
        
        
        
game = ConectFour()
game.playerNames()
game.printNames()
game.gameBoard()
game.updateBoard()
#while winner == False
n = 0
while n < 42 and game.winner == False:
    n+=1
    game.playgame()
#game.clearBoard()
    if game.winner == False:
        game.updateBoard()
