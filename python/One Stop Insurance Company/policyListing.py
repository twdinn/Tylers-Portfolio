# Policy Listing Report and Monthly Payment Report
# Written By: Tyler Dinn
# Date: April 8, 2022

import datetime as dt

today = dt.datetime.now()
today = dt.datetime.strftime(today, "%d-%m-%Y")


def DollarDSP(price):
    # Function for Formatting into Dollar values
    # Price is float value being formatted into Dollar
    DSP = "${:,.2f}".format(price)

    return DSP


# Policy Listing Report
# Counter For Total Policies
policyCtr = 0
# Accumulator For Insurance Premium
insurePremiumAcc = 0
# Accumulator For Extra Costs
extraCostAcc = 0
# Accumulator For Total Premium
totalPremiumAcc = 0

print("ONE STOP INSURANCE COMPANY")
print("POLICY LISTING AS OF {}".format(today))
print()
print("POLICY  CUSTOMER              INSURANCE     EXTRA      TOTAL")
print("NUMBER  NAME                   PREMIUM      COSTS      PREMIUM")
print("=" * 64)

# Read Policies.dat File
with open("Policies.dat", "r") as f:
    for policyDataLine in f:
        policyData = policyDataLine.split(",")
        policyNum = policyData[0].strip()
        custFirstName = policyData[2].strip()
        custLastName = policyData[3].strip()
        totalPremium = float(policyData[14].strip())
        insurPremium = float(policyData[15].strip())
        extraCosts = float(policyData[16].strip())

        # Formatted Dollar Values
        insurPremiumDsp = DollarDSP(insurPremium)
        extraCostsDsp = DollarDSP(extraCosts)
        totalPremiumDsp = DollarDSP(totalPremium)

        custNameDsp = "{} {}".format(custFirstName, custLastName)

        print("{:<4}  {:<20}   {:>10} {:>10}   {:>10}".format(policyNum, custNameDsp, insurPremiumDsp, extraCostsDsp,
                                                              totalPremiumDsp))

        policyCtr += 1
        insurePremiumAcc += insurPremium
        extraCostAcc += extraCosts
        totalPremiumAcc += totalPremium

print("=" * 64)

insurePremiumAccDsp = DollarDSP(insurePremiumAcc)
extraCostAccDsp = DollarDSP(extraCostAcc)
totalPremiumAccDsp = DollarDSP(totalPremiumAcc)

print("Total policies: {:<3}          {:>10} {:>10}   {:>10}".format(policyCtr, insurePremiumAccDsp, extraCostAccDsp,
                                                                      totalPremiumAccDsp))
print()
print()

print("-" * 76)
print()

# Monthly Payment Listing Report
# Counter For Total Policies
policyCtr = 0
# Accumulator For Total Premium
totalPremiumAcc = 0
# Accumulator For HST
hstAcc = 0
# Accumulator For Total Cost
totalCostAcc = 0
# Accumulator For Monthly Payment
monthlyPayAcc = 0

print("ONE STOP INSURANCE COMPANY")
print("MONTHLY PAYMENT LISTING AS OF {}".format(today))
print()
print("POLICY  CUSTOMER                TOTAL                   TOTAL      MONTHLY")
print("NUMBER  NAME                   PREMIUM      HST         COST       PAYMENT")
print("=" * 76)
with open("Policies.dat", "r") as f:
    for policyDataLine in f:
        policyData = policyDataLine.split(",")
        policyNum = policyData[0].strip()
        custFirstName = policyData[2].strip()
        custLastName = policyData[3].strip()
        insurPremium = float(policyData[15].strip())
        extraCosts = float(policyData[16].strip())
        totalPremium = float(policyData[14].strip())
        payMethod = policyData[13].strip()
        hst = float(policyData[17].strip())
        totalCost = float(policyData[18].strip())
        monthlyPayment = float(policyData[19].strip())

        custNameDsp = "{} {}".format(custFirstName, custLastName)

        # Formatted Dollar Values
        insurPremiumDsp = DollarDSP(insurPremium)
        extraCostsDsp = DollarDSP(extraCosts)
        totalPremiumDsp = DollarDSP(totalPremium)
        hstDsp = DollarDSP(hst)
        monthlyPaymentDsp = DollarDSP(monthlyPayment)
        totalCostDsp = DollarDSP(totalCost)

        if payMethod == "M":
            print(
                "{:<4}  {:<20}  {:>10} {:>10}    {:>10} {:>10}".format(policyNum, custNameDsp, totalPremiumDsp,
                                                                          hstDsp, totalCostDsp,
                                                                          monthlyPaymentDsp))

            policyCtr += 1
            totalPremiumAcc += totalPremium
            hstAcc += hst
            totalCostAcc += totalCost
            monthlyPayAcc += monthlyPayment

print("=" * 76)

totalPremiumAccDsp = DollarDSP(totalPremiumAcc)
hstAccDsp = DollarDSP(hstAcc)
totalCostAccDsp = DollarDSP(totalCostAcc)
monthlyPayAccDsp = DollarDSP(monthlyPayAcc)

print("Total policies: {:<3}         {:>10} {:>10}    {:>10} {:>10}".format(policyCtr, totalPremiumAccDsp, hstAccDsp,
                                                                      totalCostAccDsp, monthlyPayAccDsp))
