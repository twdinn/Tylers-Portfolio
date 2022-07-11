# Program for The St. John’s Marina & Yacht Club
# Written By: Tyler Dinn
# Date: Feb 6 2022


# Program Constants
ALT_MEM_COST = 5.00
TAX_RATE = 0.15
CANCEL_RATE = 0.60
ISSUED_DATE = "2022-02-06"
HST_REG_NO = "549-33-5849-4720-9885"

# Data Entered By Receptionist
siteNum = int(input("Enter Site Number (1-100): "))
memberNam = input("Enter Members Name: ")
strAdd = input("Enter Street Address: ")
city = input("Enter City: ")
prov = input("Enter Province (XX): ").upper()
postCode = input("Enter Postal Code (A1A1A1): ").upper()
phoneNum = input("Enter Phone Number: ")
cellNum = input("Enter Cell Number: ")
memType = input("Enter Membership Cost (S for Standard, E for Executive): ")
altMembers = int(input("Enter Alternative Members: "))
weeklySiteClean = input("Weekly Site Clean (Y for Yes, N for No): ").upper()
vidSurveil = input("Video Surveillance (Y for Yes, N for No): ").upper()

# Calculations For the Receipt
if siteNum % 2 == 0:
    siteCost = 80.00
else:
    siteCost = 120.00

siteCharge = siteCost + (altMembers * ALT_MEM_COST)

cleanCharge = 0
if weeklySiteClean == "Y":
    cleanCharge = 50.00
    weeklySiteClean = "Yes"
else:
    weeklySiteClean = "No"

vidCharge = 0
if vidSurveil == "Y":
    vidCharge = 35.00
    vidSurveil = "Yes"
else:
    vidSurveil = "No"

extraCharge = cleanCharge + vidCharge

subtotal = siteCharge + extraCharge

taxes = subtotal * TAX_RATE

totMonthlyChar = subtotal + taxes

if memType == "E":
    monthlyDues = 150.00
    memType = "Executive"
else:
    monthlyDues = 75.00
    memType = "Standard"

totMonthlyFees = totMonthlyChar + monthlyDues

totYearlyFee = totMonthlyFees * 12

monthlyPay = (totYearlyFee + 59.99) / 12

cancelFee = totYearlyFee * CANCEL_RATE


# Formatted Outputs for the Receipt
print()
print("     St.John’s Marina & Yacht Club")
print("         Yearly Member Receipt")
print("―" * 38)
print("Client Name and Address:")
print()
print("{:<25}".format(memberNam))
print("{:<25}".format(strAdd))
addressDsp = "{}, {} {}".format(city, prov, postCode)
print("{:<26}".format(addressDsp))
print()
phoneNumDsp = "{} (H)".format(phoneNum)
cellNumDsp = "{} (C)".format(cellNum)
print("Phone:  {:>10}".format(phoneNumDsp))
print("        {:>10}".format(cellNumDsp))
print()
print("Site #: {:<3}   Member type: {:>9}".format(siteNum, memType))
print()
print("Alternate members:                {:>2}".format(altMembers))
print("Weekly site cleaning:            {:>3}".format(weeklySiteClean))
print("Video surveillance:              {:>3}".format(vidSurveil))
print()
siteChargeDsp = "${:,.2f}".format(siteCharge)
print("Site charges:              {:>9}".format(siteChargeDsp))
extraChargeDsp = "${:,.2f}".format(extraCharge)
print("Extra charges:               {:>7}".format(extraChargeDsp))
print("                           ----------")
subtotalDsp = "${:,.2f}".format(subtotal)
print("Subtotal:                  {:>9}".format(subtotalDsp))
taxesDsp = "${:,.2f}".format(taxes)
print("Sales tax (HST):             {:>7}".format(taxesDsp))
print("                           ----------")
totMonthlyCharDsp = "${:,.2f}".format(totMonthlyChar)
print("Total monthly charges:     {:>9}".format(totMonthlyCharDsp))
monthlyDuesDsp = "${:,.2f}".format(monthlyDues)
print("Monthly dues:                {:>7}".format(monthlyDuesDsp))
print("                           ----------")
totMonthlyFeesDsp = "${:,.2f}".format(totMonthlyFees)
print("Total monthly fees:        {:>9}".format(totMonthlyFeesDsp))
totYearlyFeeDsp = "${:,.2f}".format(totYearlyFee)
print("Total yearly fees:        {:>10}".format(totYearlyFeeDsp))
print()
monthlyPayDsp = "${:,.2f}".format(monthlyPay)
print("Monthly payment:           {:>9}".format(monthlyPayDsp))
print()
print("―" * 38)
print()
print("Issued: {:<10}".format(ISSUED_DATE))
print("HST Reg No: {:<21}".format(HST_REG_NO))
print()
cancelFeeDsp = "${:,.2f}".format(cancelFee)
print("Cancellation fee:          {:>9}".format(cancelFeeDsp))
