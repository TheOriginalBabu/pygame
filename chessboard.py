# Filename: chessboard.py
# Description: Chessboard Program
# Author: Izaan Syed
# Energy: None
# - sorry for falling asleep in class

def sizeinput():
	global xsize
	global ysize
	try:
		xsize = int(input("Enter desired length of X Axis on rectangle shape: "))
		if xsize < 1:
			1/0

		ysize = int(input("Enter desired length of Y Axis on rectangle shape: "))
		if ysize < 1:
			1/0

	except:
		print("Invalid Input")
		print()
		sizeinput()

def squareinput():
	global xcoord
	global ycoord
	try:
		xcoord = int(input("Enter X Co-ordinate: "))
		if xcoord < 1 or xcoord > xsize:
			1/0

		ycoord = int(input("Enter Y Co-ordinate: "))
		if ycoord < 1 or ycoord > ysize:
			1/0

	except:
		print("Invalid Input")
		print()
		squareinput()

sizeinput()
squareinput()


if xcoord % 2 - ycoord % 2 == 0:
	color = "black"
else:
	color = "white"

print(f"Selected Co-ordinates ({xcoord}, {ycoord}) correspond to a {color} square")
print()

# Chess expansion

def moveinput():
	global xmove
	global ymove
	try:
		xmove = int(input("Enter X Co-ordinate of position to move to: "))
		if xmove < 1 or xmove > xsize:
			1/0

		ymove = int(input("Enter Y Co-ordinate of position to move to: "))
		if ymove < 1 or ymove > ysize:
			1/0

	except:
		print("Invalid Input")
		print()
		moveinput()

moveinput()

# Checks

# Pawn
if ycoord + 1 == ymove and xcoord == xmove:
	print("pawncandoit")
elif ycoord + 2 == ymove and xcoord == xmove:
	print("pawnmightdoitifitsthefirstmoveofitself")

# Rook
if abs((xcoord - xmove)) == 1 and ycoord == ymove or abs((ycoord - ymove)) == 1 and xcoord == xmove or xcoord == xmove or ycoord == ymove:
	print("rookcandoit")

# Horse
if abs(xcoord - xmove) == 1 and abs(ycoord - ymove) == 2 or abs(xcoord - xmove) == 2 and abs(ycoord - ymove) == 1:
	print("horsecandoit")

# Bishop
if abs((xcoord - xmove)) == abs((ycoord - ymove)):
	print("bishopcandoit")

# king
if abs((xcoord - xmove)) == 1 or abs((ycoord - ymove)) == 1:
	print("kingcandoit")