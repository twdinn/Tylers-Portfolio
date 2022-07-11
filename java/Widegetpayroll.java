// Program to Calculate Payroll of Widget Inc
// Written By: Tyler Dinn
// Date: April 29, 2022

import java.util.Scanner;

public class Widegetpayroll {
    public static void main(String[] args) {
        // Program Constants
        final double HOURLY_RATE = 17.50;
        final double COMMISSION_RATE = 0.35;
        final double INCOME_TAX_RATE = 0.21;
        final double CPP_RATE = 0.0495;
        final double EI_CONT_RATE = 0.016;
        final double UNION_DUES = 15.00;

        // Data To Be Entered By The User
        String employName;
        int hoursWorked;
        int widgetMon;
        int widgetTues;
        int widgetWed;
        int widgetThurs;
        int widgetFri;

        Scanner keyboard = new Scanner(System.in);

        System.out.print("Enter Employee Name: ");
        employName = keyboard.nextLine();
        System.out.print("Enter Hours Worked: ");
        hoursWorked = keyboard.nextInt();
        System.out.print("Enter the Number of Widgets Produced on Monday: ");
        widgetMon = keyboard.nextInt();
        System.out.print("Enter the Number of Widgets Produced on Tuesday: ");
        widgetTues = keyboard.nextInt();
        System.out.print("Enter the Number of Widgets Produced on Wednesday: ");
        widgetWed = keyboard.nextInt();
        System.out.print(("Enter the Number of Widgets Produced on Thursday: "));
        widgetThurs = keyboard.nextInt();
        System.out.print("Enter the Number of Widgets Produced on Friday: ");
        widgetFri = keyboard.nextInt();

        // Calculations For Program
        int totalWidget = widgetMon + widgetTues + widgetWed + widgetThurs + widgetFri;
        double regularPay = hoursWorked * HOURLY_RATE;
        double commission = totalWidget * COMMISSION_RATE;
        double grossPay = regularPay + commission;
        double incomeTax = grossPay * INCOME_TAX_RATE;
        double cpp = grossPay * CPP_RATE;
        double eiCont = grossPay * EI_CONT_RATE;
        double totalDeduc = incomeTax + cpp + eiCont + UNION_DUES;
        double netPay = grossPay - totalDeduc;

        // Display Results
        System.out.println();
        System.out.printf("Employee Name:                %s%n", employName);
        System.out.printf("Total Widgets Produced:              %3d%n", totalWidget);
        System.out.println("-----------------------------------------");
        String regularPayDsp = String.format("$%,.2f", regularPay);
        System.out.printf("Regular Pay:                   %9s%n", regularPayDsp);
        String commissionDsp = String.format("$%,.2f", commission);
        System.out.printf("Commission:                    %9s%n", commissionDsp);
        String grossPayDsp = String.format("$%,.2f", grossPay);
        System.out.printf("Gross Pay:                     %9s%n", grossPayDsp);
        String incomeTaxDsp = String.format("$%,.2f", incomeTax);
        System.out.printf("Income Tax:                    %9s%n", incomeTaxDsp);
        String cppDsp = String.format("$%,.2f", cpp);
        System.out.printf("CPP:                              %6s%n", cppDsp);
        String eiContDsp = String.format("$%,.2f", eiCont);
        System.out.printf("EI Contribution:                  %6s%n", eiContDsp);
        String unionDuestDsp = String.format("$%,.2f", UNION_DUES);
        System.out.printf("Union Dues:                       %6s%n", unionDuestDsp);
        String totalDeducDsp = String.format("$%,.2f", totalDeduc);
        System.out.printf("Total Deduction:               %9s%n", totalDeducDsp);
        String netPayDsp = String.format("$%,.2f", netPay);
        System.out.printf("Net Pay:                       %9s%n", netPayDsp);






     // End Main
    }
}