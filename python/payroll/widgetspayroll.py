# Program to Calculate Payroll of Widget Inc
# Written By: Tyler Dinn
# Date Jan 21 2022

# Program Constants
HOURLY_RATE = 17.50
COMMISSION_RATE= 0.35
INCOME_TAX_RATE = 0.21
CPP_RATE = 0.0495
EI_CONT_RATE = 0.016
UNION_DUES = 15.00

# Data to Be Entered By the User
employName = input("Enter Employee Name: ")
hoursWorked = int(input("Enter Hours Worked: "))
widgetMon = int(input("Enter the Number of Widgets Produced on Monday: "))
widgetTues = int(input("Enter the Number of Widgets Produced on Tuesday: "))
widgetWed = int(input("Enter the Number of Widgets Produced on Wednesday: "))
widgetThurs = int(input("Enter the Number of Widgets Produced on Thursday: "))
widgetFri = int(input("Enter the Number of Widgets Produced on Friday: "))

# Calculations for Program
totalWidget = widgetMon + widgetTues + widgetWed + widgetThurs + widgetFri
regularPay = hoursWorked * HOURLY_RATE
commission = totalWidget * COMMISSION_RATE
grossPay = regularPay + commission
incomeTax = grossPay * INCOME_TAX_RATE
cpp = grossPay * CPP_RATE
eiCont = grossPay * EI_CONT_RATE
totalDeduc = incomeTax + cpp + eiCont + UNION_DUES
netPay = grossPay - totalDeduc

# Display results
print()
print("Employee Name:            ", employName)
print("Total Widgets Produced :  ", totalWidget)
print("----------------------------------")
print("Regular Pay:             $", regularPay)
print("Commission:              $", commission)
print("Gross Pay:               $", grossPay)
print("Income Tax:              $", incomeTax)
print("CPP:                     $", cpp)
print("EI Contribution:         $", eiCont)
print("Total Deductions:        $", totalDeduc)
print("Net Pay:                 $", netPay)