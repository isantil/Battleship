import os
from games import Board
import random

cls = lambda: os.system('cls')
cls()

class Ship():

	def __init__(self,length,name):
		self.length = length
		self.alive = True
		self.name = name

	def placeShip(self,cordsList,board):
		# Cords should be a list of the coordinates where the ship is located
		for cord in cordsList:
			board.board[cord] = 'O'

def start():
	print("Welcome to battleship!!")
	gameMode = input("Select if you want to play against another player [1] or against an AI [2]: ")
	
	#setup(gameMode)
	mainGame(gameMode)

'''
def setup(gameMode):
	if gameMode == "2":
		playerBoard = Board(8,8)
		playerEnemyBoard = Board(8,8)
'''


def mainGame(gameMode):
	if gameMode == "1":
		# Code for game Player vs player
		return
	elif gameMode == "2":
		# Code for game player vs AI

		player1Board = Board(8,8)
		player1EnemyBoard = Board(8,8)

		player2Board = Board(8,8)
		player2EnemyBoard = Board(8,8)

		player1Boat = Ship(1,'Boat')
		player1Destroyer = Ship(2,'Destroyer')
		player1Submarine = Ship(3,'Submarine')
		player1Battleship = Ship(4,'Battleship')

		player2Boat = Ship(1,'Boat')
		player2Destroyer = Ship(2,'Destroyer')
		player2Submarine = Ship(3,'Submarine')
		player2Battleship = Ship(4,'Battleship')

		player1Ships = [player1Boat,player1Destroyer,player1Submarine,player1Battleship]
		player2Ships = [player2Boat,player2Destroyer,player2Submarine,player2Battleship]

		print('[PLAYER 1] Choose where you want to place your ships.')
		shipPlacement(player1Ships,player1Board)


		print('[PLAYER 2] Choose where you want to place your ships.')
		shipPlacement(player2Ships,player2Board)

		player1 = {'name':'PLAYER 1','board':player1Board,'enemy':player1EnemyBoard}
		player2 = {'name':'PLAYER 2','board':player2Board,'enemy':player2EnemyBoard}
		players = [player1,player2]

		while True:

			currentPlayer = players[0]
			currentEnemy = players[1]

			showPlayerBoard(currentPlayer)

			playerMove(currentPlayer,currentEnemy)

			showPlayerBoard(currentPlayer)

			input(f'[{currentPlayer['name']}] Press any key to finish your turn: ')

			del players[0]
			players.append(currentPlayer)

def shipPlacement(playerShips,playerBoard):
	
	for ship in playerShips:
		currentLength = 0
		locationOfShip = []
		while currentLength < ship.length:
			
			coordToPlace = input(f'Select a coordenate to place your {ship.name}. It needs {ship.length} spaces: ').upper()
			locationOfShip.append(coordToPlace)
			currentLength += 1
		ship.placeShip(locationOfShip,playerBoard)
	cls()

def playerMove(currentPlayer,currentEnemy):

	move = input(f'[{currentPlayer['name']}] Select a coordenate to attack: ').upper()
	if currentEnemy['board'].board[move] == 'O':
		currentPlayer['enemy'].board[move] = '*'
		currentEnemy['board'].board[move] = 'T'
	else:
		currentPlayer['enemy'].board[move] = 'X'
		currentEnemy['board'].board[move] = 'X'

def showPlayerBoard(player):
	cls()
	print('Your board with your ships: ')
	player['board'].display()
	print('==================================')
	print('Your board with the enemy ships: ')
	player['enemy'].display()

if __name__ == '__main__':
	start()
