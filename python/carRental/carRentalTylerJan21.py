# Program to Calculate Car Rental Bill
# Written By : Tyler Dinn
# Date: Jan 21 2022

# Program Constants
PER_DAY_CHAR = 35.00
PER_KILO_CHAR = 0.10
HST_RATE = 0.15

# Data Entered By User
custName = input("Enter Customer Name: ")
phoneNum = input("Enter Customer Phone Number: ")
numDays = int(input("Enter Number of Days the Car Was Rented: "))
rentMil= int(input("Enter the Mileage When the Car Was Rented: "))
returnMil= int(input("Enter the Mileage When the Car Was Returned: "))

# Calculations for the Program
kiloTravel = returnMil - rentMil

dailyCost = PER_DAY_CHAR * numDays
mileCost = PER_KILO_CHAR * kiloTravel
rentCost = dailyCost + mileCost
hst = dailyCost * HST_RATE
totalRentCost = rentCost + hst

# Display inputs and calculated values
print()
print("Customer Name:                      ", custName)
print("Customer Phone Number:              ", phoneNum)
print("Number of Days the Car Was Rented:  ", numDays)
print("Mileage When the Car Was Rented:    ", rentMil)
print("Mileage When the Car Was Returned   ", returnMil)
print()
print("Number of kilometers traveled:      ", kiloTravel)
print("Cost for the Rental:               $", rentCost)
print("HST:                               $", hst)
print("Total Rental Cost:                 $", totalRentCost)
