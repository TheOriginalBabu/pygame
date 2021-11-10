# Filename: chessboard.py
# Description: Chessboard Program
# Author: Izaan Syed
# Energy: None
# - sorry for falling asleep in class

# <- INPUT ->

def sizeinput(): # Input for size of chessboard
	global xsize
	global ysize
	try:
		xsize = int(input("Enter desired length of X Axis on rectangle shape: "))
		if xsize < 1: # Break condition
			1/0 

		ysize = int(input("Enter desired length of Y Axis on rectangle shape: "))
		if ysize < 1: # Break condition
			1/0

	except: # Error catching
		print("Invalid Input")
		print()
		sizeinput()

def squareinput():
	global xcoord
	global ycoord
	try:
		xcoord = int(input("Enter X Co-ordinate: "))
		if xcoord < 1 or xcoord > xsize: # Break condition
			1/0

		ycoord = int(input("Enter Y Co-ordinate: "))
		if ycoord < 1 or ycoord > ysize: # Break condition
			1/0

	except: # Error catching
		print("Invalid Input")
		print()
		squareinput()

def moveinput():
	global xmove
	global ymove
	try:
		xmove = int(input("Enter X Co-ordinate of position to move to: "))
		if xmove < 1 or xmove > xsize: # Break condition
			1/0

		ymove = int(input("Enter Y Co-ordinate of position to move to: "))
		if ymove < 1 or ymove > ysize: # Break condition
			1/0

	except: # Error catching
		print("Invalid Input")
		print()
		moveinput()

sizeinput()
squareinput()
moveinput()

# <- PROCESSING ->

if xcoord % 2 - ycoord % 2 == 0: # Square color check
	color = "black"
else:
	color = "white"

if xmove % 2 - ymove % 2 == 0: # Square color check (second selection)
	colornew = "black"
else:
	colornew = "white"

chesspieces = [] # List initialization to hold all applicable pieces

# Check if both co-ordinates the same
if ycoord == ymove and xcoord == xmove:
	print("Both sets of co-ordinates correspond to the same square. No applicable chess moves.")
	exit()

# Pawn
if ycoord + 1 == ymove and xcoord == xmove:
	chesspieces.append("Pawn")
elif ycoord + 2 == ymove and xcoord == xmove:
	chesspieces.append("Pawn")
	pawnassumption = True


# Rook
if abs((xcoord - xmove)) == 1 and ycoord == ymove or abs((ycoord - ymove)) == 1 and xcoord == xmove or xcoord == xmove or ycoord == ymove:
	chesspieces.append("Rook")

# Knight (Horse)
if abs(xcoord - xmove) == 1 and abs(ycoord - ymove) == 2 or abs(xcoord - xmove) == 2 and abs(ycoord - ymove) == 1:
	chesspieces.append("Knight")

# Bishop
if abs((xcoord - xmove)) == abs((ycoord - ymove)):
	chesspieces.append("Bishop")

# King
if abs((xcoord - xmove)) == 1 or abs((ycoord - ymove)) == 1:
	chesspieces.append("King")

# Queen (combination of either Rook, Bishop, and King)
if "Rook" in chesspieces or "Bishop" in chesspieces or "King" in chesspieces:
	chesspieces.append("Queen")

# <- OUTPUT ->

print(f"Selected Co-ordinates ({xcoord}, {ycoord}) correspond to a {color} square")
print()

print(f"Selected Co-ordinates of second position ({xmove}, {ymove}) correspond to a {colornew} square")
print()

print(f"Valid chess pieces to move to this location: {chesspieces}")

if pawnassumption == True:	# Pawn can move up two if it's its first move,
	print("Note: Assuming it's Pawn's first move")