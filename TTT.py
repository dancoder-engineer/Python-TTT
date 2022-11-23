import os
from sys import platform

board = []
whoseTurn = ""
keepPlaying = True

def initGame():
  global board
  global whoseTurn
  board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
  whoseTurn = "X"

def cls():
    if platform == "win32":
      os.system("cls")
    else:
      os.system("clear")

def printBoard():
  print (board[0]+"|"+board[1]+"|"+board[2])
  print ("-+-+-")
  print (board[3]+"|"+board[4]+"|"+board[5])
  print ("-+-+-")
  print (board[6]+"|"+board[7]+"|"+board[8])

def switchTurn():
  global whoseTurn
  if whoseTurn == "X":
    whoseTurn = "O"
  else:
    whoseTurn = "X"

def checkIfWinner():
  if (board[0] == board[1] == board[2]):
    laudWinner(board[0])
  if (board[3] == board[4] == board[5]):
    laudWinner(board[3])
  if (board[6] == board[7] == board[8]):
    laudWinner(board[6])
  if (board[0] == board[3] == board[6]):
    laudWinner(board[0])
  if (board[1] == board[4] == board[7]):
    laudWinner(board[1])
  if (board[2] == board[5] == board[8]):
    laudWinner(board[2])
  if (board[0] == board[4] == board[8]):
    laudWinner(board[0])
  if (board[2] == board[4] == board[6]):
    laudWinner(board[2])
    
def inputAndChange():
  global board
  inputWhere = input("Where do you wish to go, " + whoseTurn + ": ")
  where = int(inputWhere)
  if where > len(board):
    return 0
  if board[where - 1] == "X" or board[where - 1] == "O":
    return 0
  board[where - 1] = whoseTurn
  switchTurn()

def laudWinner(winner):
  global keepPlaying
  print("Congratulations, " + winner + ", you win!")
  morePrompt = "9"
  while morePrompt != "Y" and morePrompt != "N":
    morePrompt = input ("Do you wish to play again? Y/N: ")
    if morePrompt == "N":
      keepPlaying = False
    else:
      initGame()

initGame()

while keepPlaying:
  cls()
  printBoard()
  inputAndChange()
  checkIfWinner()