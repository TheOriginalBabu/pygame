# Authors - Jack, Izaan, Lucy, Damon
# Date - 11/10/2021
# Desc. - A way to calculate the transfer of money using alien coins.

# TODO:
# Implement correct grammar for singular coins ("1 Drobzit" instead of "1 Drobzits")
# Do not unnecessarily state coins equal to zero (instead of "0 Drobzits, 0 Clickwichs, 2 Gazoontights, 3 Frazoints" ~ display only "2 Gazoontights, 3 Frazoints")
# Currency conversions from CAD > Zircoins (can also extend to live currency rates https://www.tutorialspoint.com/python-get-the-real-time-currency-exchange-rate)

# <- Initialization ->
import math            # Used for round down function

CONST_DROBZIT = 100000 # Value of each coin, held in constant
CONST_CLICKWICH = 50000
CONST_GAZOONTIGHT = 10000
CONST_FRAZOINT = 1000
CONST_BLOINTOINT = 500
CONST_VROBIT = 1 

# <- Inputs ->

print ("Welcome to ZircoinFinancial!")

def moneyinput():      # Error trapped function to get withdrawal amount input
    global cashmoney
    try:
        cashmoney = int(input("How much money would you like to withdraw? "))
    except:
        print("Invalid input")
        print()
        moneyinput()
    print()

moneyinput()

#exchangein = input("What currency is being traded in? 1 for canadian dolars, 2 for this alien shit")
#exchangeout = input("What currency is to be returned? 1 for candian dolars, 2 for this alien shit")

# <- Processing ->

drobzit_value = int(math.floor(cashmoney/CONST_DROBZIT)) # Divides withdrawal amount by coin value, then rounds down to get the largest amount of coins possible
cashmoney = cashmoney -  drobzit_value * CONST_DROBZIT   # Removes value of coins that are already withdrawn

clickwich_value = int(math.floor(cashmoney / CONST_CLICKWICH)) 
cashmoney = cashmoney -  clickwich_value * CONST_CLICKWICH

gazoontight_value = int(math.floor(cashmoney / CONST_GAZOONTIGHT))
cashmoney = cashmoney - gazoontight_value * CONST_GAZOONTIGHT

frazoint_value = int(math.floor(cashmoney / CONST_FRAZOINT))
cashmoney = cashmoney - frazoint_value * CONST_FRAZOINT

blointoint_value = int(math.floor(cashmoney / CONST_BLOINTOINT))
cashmoney = cashmoney - blointoint_value * CONST_BLOINTOINT

vrobit_value = int(math.floor(cashmoney / CONST_VROBIT))
cashmoney = cashmoney - vrobit_value * CONST_VROBIT

# <- Output ->

print(f"{drobzit_value} drobzits, {clickwich_value} clickwichs, {gazoontight_value} gazoontights, {frazoint_value} frazoints, {blointoint_value} blointoints, {vrobit_value} vrobits")
# ^ above output format is placeholder please dont actually keep this