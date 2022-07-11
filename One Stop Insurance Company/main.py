# Program For One Stop Insurance Company
# Written By: Tyler Dinn
# Date: April 8, 2022

import datetime as dt


def DollarDSP(price):
    # Function for Formatting into Dollar values
    # Price is float value being formatted into Dollar
    DSP = "${:,.2f}".format(price)

    return DSP


# Read OSICDef.dat File
with open("OSICDef.dat", "r") as f:
    NEXT_POLICY_NO = int(f.readline())
    BASIC_PREMIUM = float(f.readline())
    ADD_CARS_DISCOUNT = float(f.readline())
    EX_LIABILITY_COV = float(f.readline())
    GLASS_COVER = float(f.readline())
    LOAN_CAR = float(f.readline())
    HST_RATE = float(f.readline())
    PROCESSING_FEE = float(f.readline())

while True:

    # Inputs and Validations
    # Customers First Name
    while True:
        custFirstName = input("Enter Customer's First Name (Type END to quit): ").title()
        if custFirstName == "":
            print("First Name Cannot Be Left Blank - Please Re-Enter")
        elif custFirstName.upper() == "END":
            exit()
        else:
            break
    # Customers Last Name
    while True:
        custLastName = input("Enter Customer's Last Name: ").title()
        if custLastName == "":
            print("Last Name Cannot Be Left Blank - Please Re-Enter")
        else:
            break
    # Customers Address
    stAdd = input("Enter Address: ").title()
    city = input("Enter City: ").title()
    prov = input("Enter Province (XX): ").upper()
    postalCode = input("Enter Postal Code (A1A1A1): ").upper()

    # Customers Phone Number
    while True:
        phoneNum = input("Enter Customers Phone Number (10 digits 9999999999): ")
        if phoneNum == "":
            print("Phone Number Can't be Blank - Please Re-Enter ")
        elif len(phoneNum) != 10:
            print("Phone Number Must be 10 Digits - Please Re-Enter")
        elif phoneNum.isdigit() == False:
            print("Phone Number Must be Digits Only - Please Re-Enter")
        else:
            break

    # Number Of Car to Be Insured
    while True:
        try:
            numCarsInsured = int(input("Enter the Number of Cars Being Insured: "))
        except:
            print("Number of Cars is Invalid - Please Re-Enter")
        else:
            break

    # Extra Liability Up to $1,000,000
    while True:
        extraLiability = input("Extra Liability Up to $1,000,000 (Enter Y for Yes or N for No: ").upper()
        if extraLiability == "Y" or extraLiability == "N":
            break
        else:
            print("Invalid Option")

    # Optional Glass Coverage
    while True:
        glassCoverage = input("Optional Glass Coverage (Y or N): ").upper()
        if glassCoverage == "Y" or glassCoverage == "N":
            break
        else:
            print("Invalid Option")

    # Optional Loaner Car
    while True:
        lonerCar = input("Optional Loaner Car (Y or N): ").upper()
        if lonerCar == "Y" or lonerCar == "N":
            break
        else:
            print("Invalid Option")

    # Pay in Full or Monthly
    while True:
        payMethod = input("Would You Like to Pay in Full or Monthly (F or M): ").upper()
        if payMethod == "F" or payMethod == "M":
            break
        else:
            print("Invalid Option")

    # $869.00 for the first automobile. Each additional automobile offered at a discount of 25%
    if numCarsInsured == 1:
        premium = BASIC_PREMIUM
    else:
        discount = BASIC_PREMIUM * ADD_CARS_DISCOUNT
        premium = BASIC_PREMIUM + ((BASIC_PREMIUM - discount) * (numCarsInsured - 1))

    # $130.00 per car for extra liability
    libCharge = 0
    if extraLiability == "Y":
        libCharge = EX_LIABILITY_COV * numCarsInsured
        extraLiability = "Yes"
    else:
        extraLiability = "No"

    # $86.00 per car for glass coverage
    glassCharge = 0
    if glassCoverage == "Y":
        glassCharge = GLASS_COVER * numCarsInsured
        glassCoverage = "Yes"
    else:
        glassCoverage = "No"

    # $58.00 per car for the loaner car
    lonerCarCharge = 0
    if lonerCar == "Y":
        lonerCarCharge = LOAN_CAR * numCarsInsured
        lonerCar = "Yes"
    else:
        lonerCar = "No"

    totalExtraCost = libCharge + glassCharge + lonerCarCharge
    totalInsurPremium = premium + totalExtraCost
    HST = HST_RATE * totalInsurPremium
    totalCost = totalInsurPremium + HST

    monthlyCost = 0
    if payMethod == "M":
        # Monthly payment by adding a processing fee of $39.99 to the total cost and dividing the total cost by 12.
        monthlyCost = (totalCost + 39.99) / 12
    else:
        totalCost

    # DateDsp
    dateIssued = dt.datetime.now()
    dateIssued = dt.datetime.strftime(dateIssued, "%m-%d-%Y")

    # Customer DSP
    nameDsp = "{} {}".format(custFirstName, custLastName)
    locationDsp = "{}, {}, {}".format(city, prov, postalCode)

    # Dollar Value DSP
    monthlyCostDsp = DollarDSP(monthlyCost)
    totalExtraCostDsp = DollarDSP(totalExtraCost)
    premiumDsp = DollarDSP(premium)
    totalInsurPremiumDsp = DollarDSP(totalInsurPremium)
    HSTDsp = DollarDSP(HST)
    totalCostDsp = DollarDSP(totalCost)

    print()
    print("    One Stop Insurance Company ")
    print("  New Insurance Policy Information")
    print()
    print("Date: {}     Policy #: {}".format(dateIssued, NEXT_POLICY_NO))
    print("―" * 36)
    print("Customer:")
    print("             {:<20} ".format(nameDsp))
    print("             {:<10}".format(phoneNum))
    print("            {:<20}".format(stAdd))
    print("         {:<30}".format(locationDsp))
    print("=" * 36)
    print("Number of Cars Insured:           {:>2}".format(numCarsInsured))
    print("Extra Liability:                 {:>3}".format(extraLiability))
    print("Glass Coverage:                  {:>3}".format(glassCoverage))
    print("Loaner Car:                      {:>3}".format(lonerCar))
    print("=" * 36)
    print("Premium:                  {:>10}".format(premiumDsp))
    print("Total Extra Costs:         {:>9}".format(totalExtraCostDsp))
    print("Total Insurance Premium:  {:>10}".format(totalInsurPremiumDsp))
    print("HST:                      {:>10}".format(HSTDsp))
    print("Total Cost:               {:>10}".format(totalCostDsp))
    print("=" * 36)
    if payMethod == "M":
        print("Monthly Payment:          {:>10}".format(monthlyCostDsp))

    # Append to Policies.dat File
    with open("Policies.dat", "a") as f:
        f.write("{}, ".format(str(NEXT_POLICY_NO)))
        f.write("{}, ".format(dateIssued))
        f.write("{}, ".format(custFirstName))
        f.write("{}, ".format(custLastName))
        f.write("{}, ".format(stAdd))
        f.write("{}, ".format(city))
        f.write("{}, ".format(prov))
        f.write("{}, ".format(postalCode))
        f.write("{}, ".format(phoneNum))
        f.write("{}, ".format(str(numCarsInsured)))
        f.write("{}, ".format(extraLiability))
        f.write("{}, ".format(glassCoverage))
        f.write("{}, ".format(lonerCar))
        f.write("{}, ".format(payMethod))
        f.write("{}, ".format(str(totalCost)))

        # Added to file for Policy Listing and Monthly Payment Reports

        f.write("{}, ".format(str(premium)))
        f.write("{}, ".format(str(totalExtraCost)))
        f.write("{}, ".format(str(HST)))
        f.write("{}, ".format(str(totalCost)))
        f.write("{}\n".format(str(monthlyCost)))

    NEXT_POLICY_NO += 1
    print("Policy processed and saved.")
    print()

    # Write to OSICDef.dat File
    with open("OSICDef.dat", "w") as f:
        f.write("{}\n".format(str(NEXT_POLICY_NO)))
        f.write("{}\n".format(str(BASIC_PREMIUM)))
        f.write("{}\n".format(str(ADD_CARS_DISCOUNT)))
        f.write("{}\n".format(str(EX_LIABILITY_COV)))
        f.write("{}\n".format(str(GLASS_COVER)))
        f.write("{}\n".format(str(LOAN_CAR)))
        f.write("{}\n".format(str(HST_RATE)))
        f.write("{}\n".format(str(PROCESSING_FEE)))

    # Bonus
    # Add the customer initials at the end of the policy number
    policyNum = "{}-{}{}".format(NEXT_POLICY_NO, custFirstName[0], custLastName[0])
    print("Policy Number: {}".format(policyNum))

    newDate = dt.datetime.strptime(dateIssued, "%m-%d-%Y")
    firstMonth = newDate.month + 1
    secondMonth = newDate.month + 2
    firstMonthYear = newDate.year

    # The first monthly payment date will be the beginning of the next month
    # If it is after the 25th, the first payment date will be the following month.
    if newDate.day <= 25:
        firstOfMonth = dt.date(month=firstMonth, day=1, year=firstMonthYear)
        firstOfMonth = dt.datetime.strftime(firstOfMonth, "%m-%d-%Y")

    else:
        firstOfMonth = dt.date(month=secondMonth, day=1, year=firstMonthYear)
        firstOfMonth = dt.datetime.strftime(firstOfMonth, "%m-%d-%Y")

    print("First Payment is Due: {}".format(firstOfMonth))
    print()
    print()
