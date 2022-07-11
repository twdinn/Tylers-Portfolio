# Program for NL Chocolate Company
# Written by: Tyler Dinn & Eoin Hurley
# Date: March 6, 2022

import matplotlib.pyplot as plt
import datetime

# Functions for Program


def TravelClaim():
    # Asks user for info regarding a travel based claim.
    # Depending on dates and several other variables, bonuses may be added.
    # At the end, a calculation will be made and printed.
    EmployeeName = input("Enter your name:                                  ")
    EmployeeLastName = input("Enter your last name:                             ")
    EmployeeNumber = input("Enter a 5 digit employee number:                  ")
    import datetime
    while True:
        try:
            StartDate = input("Enter the start date of the claim (YYYY-MM-DD):   ")
            StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
        except:
            print("Start date not a valid format - Please re-enter.")
        else:
            break
    while True:
        try:
            EndDate = input("Enter the end date of the claim (YYYY-MM-DD):     ")
            EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
        except:
            print("End date not a valid format - Please re-enter. ")
        else:
            if EndDate <= StartDate:
                print("End date must be after the start date - Please re-enter. ")
            else:
                break
    NumDays = (EndDate - StartDate).days

    TripLocation = input("Enter the location of your trip:                  ")
    TotalKilometers = int(input("Enter how many kilometers you traveled:           "))
    OwnershipStatus = input("Enter whether you own or rent your vehicle (O/R): ")
    if OwnershipStatus == "O":
        MileageAmount = TotalKilometers * 0.17
        OwnershipBonus = 0.04 * TotalKilometers
    elif OwnershipStatus == "R":
        MileageAmount = 65.00 * NumDays
        OwnershipBonus = 0
    else:
        OwnershipStatus = input("Please enter a valid status:                      ")

    ClaimType = input("Is your claim Standard or Executive? (S/E):       ")
    if ClaimType == "S":
        ExecutiveBonus = 45.00 * NumDays
    else:
        ExecutiveBonus = 0

    # Calculations to determine final numbers for the print region.
    if NumDays > 3:
        ExtraDaysBonus = 100
    else:
        ExtraDaysBonus = 0

    PerDiemAmount = NumDays * 85.00
    HST = PerDiemAmount * 0.15
    Bonus = (ExecutiveBonus + OwnershipBonus)
    ClaimAmount = PerDiemAmount + MileageAmount + Bonus
    ClaimTotal = ClaimAmount + HST

    # Print region where final numbers are displayed.
    print("Final outcome:")
    print("Employee name:       ", EmployeeName, EmployeeLastName)
    print("Employee #:          ", EmployeeNumber)
    print("Travel location:     ", TripLocation)
    print("Start and finish date:", StartDate, ",", EndDate)
    print("")
    print("Per diem amount:     ", PerDiemAmount)
    print("Claim amount:        ", ClaimAmount)
    print("Bonus:               ", Bonus)
    print("HST:                 ", HST)
    print("                     ------------")
    print("Claim total:         ", ClaimTotal)
    print(" ")

    any = input("Enter any key to continue... ")


def InterviewQues():
    # Creates a loop 1-100.
    # If the number is divisible by 5 display the word Fizz.
    # If the value is divisible by 8 display the word Buzz.
    # If the value is divisible by both 5 and 8 display the word FizzBuzz.
    # Otherwise, display just the number

    for num in range(1, 101):
        if num % 5 == 0 and num % 8 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Fizz")
        elif num % 8 == 0:
            print("Buzz")
        else:
            print(num)
    print()
    any = input("Press any key to continue... ")


def StringsAndDates():
    print("Input your birthday below to receive a birthday discount code usable on that date.")
    print("This code is unique to you and gives a one-time birthday discount, so don't share it with anybody.")
    print(" ")
    EmployeeName = input("Enter your first name:                                ")
    EmployeeLastName = input("Enter your last name:                                 ")
    EmployeePhone = input("Enter your phone number:                              ")

    while True:
        try:
            Birthday = input("Enter your upcoming birthday (example: 2022-01-01):   ")
            Birthday = datetime.datetime.strptime(Birthday, "%Y-%m-%d")
        except:
            print("Birthday not a correct entry. Please re-enter:        ")
        else:
            break
    Now = datetime.datetime.now()
    TilBirthday = Birthday - Now
    DiscountCode = "{}{}{}-{}".format(EmployeeName[0], EmployeeLastName[0], EmployeePhone[6:10], Birthday)
    print("Time until your birthday:                             ", TilBirthday)
    print("Use your code listed below on ", Birthday, ".")
    print("Birthday company-wide discount code:                  ", DiscountCode)
    any = input("Press any key to continue... ")


def MonthlyClaimTotals():
    # A line graph to show monthly claim totals
    # X Axis = months from Jan - Dec
    # Y Axis = Monthly Totals added by user
    xAxis = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
    yAxis = []

    for x in range(12):
        while True:
            try:
                monthlyTotals = float(input(f"Enter Monthly For Total {xAxis[x]}: "))
            except:
                print("Monthly Total is Invalid - Please Re-Enter")
            else:
                break
        yAxis.append(monthlyTotals)

    plt.plot(xAxis, yAxis, color="Red", marker="o")

    plt.xlabel('Months')
    plt.ylabel('Monthly Totals')

    plt.title('Monthly Claim Total')
    plt.grid(True)

    plt.show()

    print()
    any = input("Enter any key to continue... ")


def Quit():
    exit()


def ChocolateBarPrice(chocPrice, numBars):
    # Calculates Total Price of Chocolate Bar Bought
    # Parameters = chocPrice, numBars
    # Parameter chocPrice is the Price of the Bar
    # Parameter numBars is How Many Bar are Bought
    # Tax of 15% Added to Price
    totalPrice = chocPrice * numBars
    totalPriceWithTax = totalPrice * 1.15

    totalPriceWithTaxDsp = "S{:,.2f}".format(totalPriceWithTax)

    return totalPriceWithTaxDsp


def EmployeeGreeting(name):
    # Sends Greeting to New Employees
    # Parameter = name (Employee's Name)
    return f"Welcome to the NL Chocolate Company Family {name}"

# Main Programs Starts Here
# Menu
while True:
    print("NL Chocolate Company")
    print("Travel Claims Processing System")
    print()
    print(
        "1. Enter an Employee Travel Claim\n" +
        "2. Fun Interview Question.\n" +
        "3. Cool Stuff with Strings and Dates.\n" +
        "4. Graph Monthly Claim Totals.\n" +
        "5. Quit the Program"
    )
    print()

    while True:
        try:
            choice = int(input("Enter choice (1-5): "))
        except:
            print("Choice is Invalid - PLease Re-Enter")
        else:
            if choice < 1 or choice > 5:
                print("Choices are (1 - 5) - Please Re-Enter ")
            else:
                break
    print()
    if choice == 1:
        TravelClaim()
    elif choice == 2:
        InterviewQues()
    elif choice == 3:
        StringsAndDates()
    elif choice == 4:
        MonthlyClaimTotals()
    elif choice == 5:
        Quit()
    else:
        print("Not a Choice")

    print()