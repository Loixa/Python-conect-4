class ConectFour:
    currentGame = {}
    def __init__(self, player1, player2):
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
       
    def playChip(self,chip,positionLetter,positionNum):
        position = []
        position = self.currentGame[positionLetter]


        if int(positionNum) % 2 ==0 and int(positionNum)>0 or int(positionNum)==1:
            position[int(positionNum)] = chip
            
        
        self.currentGame[positionLetter] = position
        
    def updateBoard(self):
        for value in self.currentGame.values():
            print(*value,sep="")







game = ConectFour("Andy", "Nikole")
game.printNames()
game.gameBoard()
game.playChip("X","G","1")
game.updateBoard()