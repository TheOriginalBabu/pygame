#Authors - Jack, Izaan, Lucy, Damon
#Date - 11/10/2021
#Desc. - A way to calculate the transfer of money using alien money.

print ("Welcome to ZircoinFinancial!")

try:
    cashmoney = int(input("How many coins are to be traded? "))
except:
    print("invalid input")

currencychoice = ["Vrobits","CAD"]

Drobzit = 100000 
Clickwich = 50000
Gazoontight = 10000
Frazoint = 1000
Blointoint = 500
Vrobit = 1 


exchangein = input("What currency is being traded in? ")
exchangeout = input("What currency is to be returned? ")

if exchangein == True and exchangeout == True:
    print ("Moving to calculations...")
elif exchangein == True and exchangeout == False:
    print ("Invalid return currency. Please reenter.")
elif exchangein == False and exchangeout == True:
    print ("Invalid currency input. Please reenter.")
elif exchangein == False and exchangeout == False:
    print ("Inputs invalid. Please try again.")
else:
    print ("What are you doing? Enter a number, a valid one, please.")