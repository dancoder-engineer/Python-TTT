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
  winningstates = ["012", "345", "678", "036", "147", "258", "048", "246"]
  for i in winningstates:
    if (board[int(i[0])] == board[int(i[1])] == board[int(i[2])]):
      laudWinner(board[int(i[0])])
  tie = True
  for i in board:
    if i != "X" and i != "O":
        tie = False
  if not tie:
    return 0
  else:
    youTied()

def askIfAgain():
  global keepPlaying
  morePrompt = ""
  while morePrompt != "Y" and morePrompt != "N":
    morePrompt = input ("Do you wish to play again? Y/N: ")
    if morePrompt == "N":
      keepPlaying = False
    else:
      initGame()

def youTied():
    print("The game is a tie.")
    askIfAgain()

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
  print("Congratulations, " + winner + ", you win!")
  askIfAgain()

def main():
  initGame()

  while keepPlaying:
    cls()
    printBoard()
    inputAndChange()
    checkIfWinner()

main()