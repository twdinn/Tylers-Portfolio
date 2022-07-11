# Program For Honest Harry Used Car Lot
# Written By: Tyler Dinn
# Date: Feb 23, 2022

import datetime as dt

# Program Constants
TAX_RATE = 0.15
TRANSFER_FEE_RATE = 0.01
LUXURY_TAX_RATE = 0.016
FINAC_FEE = 39.99


def DollarDSP(price):
    # Function for Formatting into Dollar values
    # Price is float value being formatted into Dollar
    DSP = "${:,.2f}".format(price)

    return DSP


# Program Inputs with Validations
while True:

    while True:
        try:
            invoiceDate = input("Enter the Date of the Invoice: ")
            invoiceDate = dt.datetime.strptime(invoiceDate, "%Y-%m-%d")
        except:
            print("Invalid Date - Please Re-Enter")
        else:
            break

    while True:
        custFirstName = input("Enter Customers First Name: ").title()
        if custFirstName == "":
            print("First Name Cannot be Blank - Please - Re-Enter")
        else:
            break

    while True:
        custLastName = input("Enter Customers Last Name: ").title()
        if custLastName == "":
            print("Last Name Cannot be Blank - Please Re-Enter")
        else:
            break

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

    streetAdd = input("Enter Street Address: ").title()
    city = input("Enter City: ").title()
    prov = input("Enter Province (XX): ").upper()
    postCode = input("Enter Postal Code (A1A1A1): ").upper()

    while True:
        plateNum = input("Enter Plate Number (XXX999): ").upper()
        if plateNum == "":
            print("Plate Number Can't be Blank - Please Re-Enter")
        elif len(plateNum) != 6:
            print("Plate Number must be 6 Characters (XXX999) - Please Re-Enter")
        elif plateNum[0:3].isalpha() == False:
            print("Plate Number Must Start With 3 Letters (XXX999) - Please Re-Enter")
        elif plateNum[3:6].isdigit() == False:
            print("Plate Number Must End With 3 Digits (XXX999) - Please Re-Enter")
        else:
            break

    carMake = input("Enter Make of Car (ie: Toyota): ").title()
    carModel = input("Enter Model of Car (ie: Corolla): ").title()
    carYear = input("Enter Year of car (ie: 2018): ")

    while True:
        try:
            sellingPrice = float(input("Enter the Selling Price (does not exceed $50,000.00): "))
        except:
            print("Selling Price is Invalid - Please Re-Enter")
        else:
            if sellingPrice > 50000.00:
                print("Selling Price Cannot Exceed $50,000.00 ")
            else:
                break

    while True:
        try:
            tradeAmt = float(input("Enter the Amount of Trade In (does not exceed the selling price): "))
        except:
            print("Trade Amount is Invalid - Please Re-Enter")
        else:
            if tradeAmt > sellingPrice:
                print("Trade Amount Cannot Exceed the Selling Price - Please Re-Enter ")
            else:
                break

    salePerName = input("Enter Salespersons Name: ").title
    creditCard = input("Enter Credit card Number (16 Digits): ")
    expiryDate = input("Enter the Expiry Date (4 Digits): ")

    priceAfTrade = sellingPrice - tradeAmt
    tax = sellingPrice * TAX_RATE

    if sellingPrice <= 5000.00:
        licenceFee = 75.00
    else:
        licenceFee = 165.00

    transferFee = sellingPrice * TRANSFER_FEE_RATE

    if sellingPrice > 20000.00:
        luxTax = sellingPrice * LUXURY_TAX_RATE
        transferFee += luxTax

    totalSalPrice = priceAfTrade + tax + licenceFee + transferFee

    print()

    # Payment Schedule
    print("# Years    # Payments    Financing Fee    Total Price  Monthly Payment")
    print("----------------------------------------------------------------------")

    for year in range(1, 5):
        numYear = year
        numMonth = year * 12
        yearFinacFee = year * FINAC_FEE
        totalPrice = totalSalPrice + yearFinacFee
        monthlyPay = totalPrice / numMonth

        yearFinacFeeDsp = DollarDSP(yearFinacFee)
        totalPriceDsp = DollarDSP(totalPrice)
        monthlyPayDsp = DollarDSP(monthlyPay)

        print(
            "    {:<1}           {:<2}            {:>7}      {:>10}       {:>9}".format(year, numMonth, yearFinacFeeDsp,
                                                                                        totalPriceDsp, monthlyPayDsp))

    print()

    while True:
        try:
            paySchedule = int(input("Enter the Payment Schedule you want to follow (1-4): "))
        except:
            print("Choice is Invalid (1-4) - Please Re-Enter")
        else:
            if paySchedule < 1 or paySchedule > 4:
                print("Choice is Invalid (1-4) - Please Re-Enter")
            else:
                break
    print()

    # Invoice Date DSP
    invoiceDateDsp = dt.datetime.strftime(invoiceDate, "%B %d, %Y")

    # Sold To DSP
    custNameDsp = "{}. {}".format(custFirstName[0], custLastName)
    locationDsp = "{}, {}, {}".format(city, prov, postCode)

    # Car Details DSP
    carDetails = "{} {} {}".format(carYear, carMake, carModel)

    # Receipt ID DSP
    receiptNo = "{}{}-{}-{}".format(custFirstName[0], custLastName[0], plateNum[3:6], phoneNum[6:10])

    # Receipt Dollar Values Formatted
    sellingPriceDsp = DollarDSP(sellingPrice)
    tradeAmtDsp = DollarDSP(tradeAmt)
    priceAfTradeDsp = DollarDSP(priceAfTrade)
    taxDsp = DollarDSP(tax)
    licenceFeeDsp = DollarDSP(licenceFee)
    transferFeeDsp = DollarDSP(transferFee)

    yearFinacFee = paySchedule * FINAC_FEE
    yearFinacFeeDsp = DollarDSP(yearFinacFee)
    totalPrice = totalSalPrice + yearFinacFee
    totalPriceDsp = DollarDSP(totalPrice)

    # Payment Details
    totalPayments = paySchedule * 12
    monthPay = totalPrice / totalPayments
    monthPayDsp = DollarDSP(monthPay)

    # First Payment Date
    payDate = invoiceDate + dt.timedelta(days=30)
    paymentDate = dt.datetime.strftime(payDate, "%d-%b-%y")

    print()
    print("         Honest Harry Car Sales")
    print("        Used Car Sale and Receipt")
    print()

    print("Invoice Date: {:<15}".format(invoiceDateDsp))
    print("Receipt No: {:<11}".format(receiptNo))
    print()
    print("Sold to:")
    print("     {:<33}".format(custNameDsp))
    print("     {:<33}".format(streetAdd))
    print("     {:<33}".format(locationDsp))
    print()
    print("Car Details: ")
    print("     {:<33}".format(carDetails))
    print("--------------------------------------")
    print("Sale price:                 {:>10}".format(sellingPriceDsp))
    print("Trade Allowance:            {:>10}".format(tradeAmtDsp))
    print("Price after Trade:          {:>10}".format(priceAfTradeDsp))
    print("                            ----------")
    print("HST:                        {:>10}".format(taxDsp))
    print("License Fee:                {:>10}".format(licenceFeeDsp))
    print("Transfer Fee:               {:>10}".format(transferFeeDsp))
    print("Financing Fee               {:>10}".format(yearFinacFeeDsp))
    print("                            ----------")
    print("Total Sales Cost:           {:>10}".format(totalPriceDsp))
    print("--------------------------------------")
    print("Terms: {:<1}            Total payments: {:>2}".format(paySchedule, totalPayments))
    print("Monthly payments:            {:>9}".format(monthPayDsp))
    print("First payment date:          {:>9}".format(paymentDate))
    print()
    print("    Honest Harry Car Sales")
    print("Best used cars at the best price!")
    print()

    contin = input("Would you Like to Enter Another Sale? (Y/N): ").upper()
    if contin == "N":
        exit()
