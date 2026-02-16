import os
import time
class ConectFour:
    currentGame = {}
    turn = 1
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
            if check[1] == " ":
                letter = "F"
                break
            check = self.currentGame["E"]
            if check[1] == " ":
                letter = "E"
                break
            check = self.currentGame["D"]
            if check[1] == " ":
                letter = "D"
                break
            check = self.currentGame["C"]
            if check[1] == " ":
                 letter = "C"
                 break
            check = self.currentGame["B"]
            if check[1] == " ":
                 letter = "B"
                 break
            check = self.currentGame["A"]
            if check[1] == " ":
                 letter = "A"
                 break
        
        return letter
    
    
    
    def updateBoard(self):
        for value in self.currentGame.values():
            print(*value,sep="")

    def clearBoard(self):
            os.system('cls' if os.name == 'nt' else 'clear')
        
    
    def playerInput(self, playerIn):
            play = input(playerIn + " choose a number to play:")
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



game = ConectFour()
game.playerNames()
game.printNames()
game.gameBoard()
game.updateBoard()
game.playgame()
