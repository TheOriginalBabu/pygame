#Authors - Jack, Izaan, Lucy, Damon
#Date - 11/10/2021
#Desc. - A way to calculate the transfer of money using alien money.

print ("Welcome to ZircoinFinancial!")

try:
    cashmoney = int(input("How many coins are to be traded? "))
except:
    print("invalid input")

currencychoice = ["Vrobits","Blointoint","Frazoint","Gazoontight","Clickwick","Drobzit"]
Vrobit = 1 
Drobzit = 100000 
Clickwich = 50000
Gazoontight = 10000
Frazoint = 1000
Blointoint = 500

exchange = input ("What currency is being traded in? ")
exchange1 = input ("What currency is to be returned? ")
if exchange == True and exchange1 == True:
    print ("Moving to calculations...")
elif exchange == True and exchange1 == False:
    print ("Invalid return currency. Please reenter.")
elif exchange == False and exchange1 == True:
    print ("Invalid currency input. Please reenter.")
elif exchange == False and exchange1 == False:
    print ("Inputs invalid. Please try again.")
else:
    print ("What are you doing? Enter a number, a valid one, please.")

if cashmoney%Drobzit == 0
    and cashmoney%Clickwich == 0
    and cashmoney%Gazoontight == 0
    and cashmoney%Frazoint == 0
    and cashmoney%Blointoint == 0: 
return Vrobits #i have no idea how to do this 

print ("Your return is ")