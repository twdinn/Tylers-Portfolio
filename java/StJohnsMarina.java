// Program for The St. John’s Marina & Yacht Club
// Written By: Tyler Dinn
// Date: Feb 6 2022

import java.util.Scanner;

public class StJohnsMarina {
    public static void main(String[] args) {
        // Program Constants
        double ALT_MEM_COST = 5.00;
        double TAX_RATE = 0.15;
        double CANCEL_RATE = 0.60;
        String ISSUED_DATE = "2022-02-06";
        String HST_REG_NO = "549-33-5849-4720-9885";

        // Data Enter By Receptionist
        int siteNum;
        String memberNam;
        String stAdd;
        String city;
        String prov;
        String postCode;
        String phoneNum;
        String cellNum;
        String memType;
        int altMember;
        String weeklySiteClean;
        String vidSurveil;

        Scanner keyboard = new Scanner(System.in);
        System.out.print("Enter Site Number (1-100):  ");
        siteNum = keyboard.nextInt();
        keyboard.nextLine();
        System.out.print("Enter Members Name: ");
        memberNam = keyboard.nextLine();
        System.out.print("Enter Street Address: ");
        stAdd = keyboard.nextLine();
        System.out.print("Enter City: ");
        city = keyboard.nextLine();
        System.out.print("Enter Province (XX): ");
        prov = keyboard.nextLine().toUpperCase();
        System.out.print("Enter Postal Code (A1A1A1): ");
        postCode = keyboard.nextLine().toUpperCase();
        System.out.print("Enter Phone Number: ");
        phoneNum = keyboard.nextLine();
        System.out.print("Enter Cell Number: ");
        cellNum = keyboard.nextLine().toUpperCase();
        System.out.print("Enter Membership Cost (S for Standard, E for Executive): ");
        memType = keyboard.nextLine().toUpperCase();
        System.out.print("Enter Alternative Members: ");
        altMember = keyboard.nextInt();
        keyboard.nextLine();
        System.out.print("Weekly Site Clean (Y for Yes, N for No): ");
        weeklySiteClean = keyboard.nextLine().toUpperCase();
        System.out.print("Video Surveillance (Y for Yes, N for No): ");
        vidSurveil = keyboard.nextLine().toUpperCase();


        // Calculations For the Receipt
        double siteCost;

        if (siteNum % 2 == 0) {
            siteCost = 80.00;
        } else {
            siteCost = 120.00;
        }

        double siteCharge = siteCost + (altMember * ALT_MEM_COST);

        double cleanCharge = 0;
        if (weeklySiteClean.equals("Y")) {
            cleanCharge = 50.00;
            weeklySiteClean = "Yes";
        } else {
            weeklySiteClean = "No";
        }

        double vidCharge = 0;
        if (vidSurveil.equals("Y")) {
            vidCharge = 35.00;
            vidSurveil = "Yes";
        } else {
            vidSurveil = "No";
        }

        double extraCharge = cleanCharge + vidCharge;
        double subtotal = siteCharge + extraCharge;
        double taxes = subtotal * TAX_RATE;double totMonthlyChar = subtotal + taxes;

        double monthlyDues = 0;
        if (memType.equals("E")) {
            monthlyDues = 150.00;
            memType = "Executive";
        }
        else {
            monthlyDues = 75.00;
            memType = "Standard";
        }

        double totMonthlyFees = totMonthlyChar + monthlyDues;
        double totYearlyFee = totMonthlyFees * 12;
        double monthlyPay = (totYearlyFee + 59.99) / 12;
        double cancelFee = totYearlyFee * CANCEL_RATE;


        // Formatted Outputs for the Receipt
        System.out.println();
        System.out.println("     St.John’s Marina & Yacht Club");
        System.out.println("         Yearly Member Receipt");
        System.out.println("――――――――――――――――――――――――――――――――――――――");
        System.out.println("Client Name and Address:");
        System.out.println();
        System.out.printf("%s%n", memberNam );
        System.out.printf("%s%n", stAdd);
        String addressDsp = city + ", " + prov + ", " + postCode;
        System.out.printf("%s%n", addressDsp);
        System.out.println();
        String phoneNumDsp = phoneNum + " " + "(H)";
        String cellNumDsp = cellNum + " " + "(C)";
        System.out.printf("Phone:" + " %10s%n", phoneNumDsp);
        System.out.printf("       %10s%n", cellNumDsp);
        System.out.println();
        System.out.printf("Site #: %2d   Member type: %10s%n", siteNum, memType);
        System.out.println();
        System.out.printf("Alternate members:                 %2d%n",altMember);
        System.out.printf("Weekly site cleaning:             %3s%n", weeklySiteClean);
        System.out.printf("Video surveillance:               %3s%n", vidSurveil);
        System.out.println();
        String siteChargeDsp = String.format("$%,.2f", siteCharge);
        System.out.printf("Site charges:              %10s%n", siteChargeDsp);
        String extraChargeDsp = String.format("$%,.2f", extraCharge);
        System.out.printf("Extra charges:             %10s%n", extraChargeDsp);
        System.out.println("                           ----------");
        String subtotalDsp = String.format("$%,.2f", subtotal);
        System.out.printf("Subtotal:                  %10s%n", subtotalDsp);
        String taxesDsp = String.format("$%,.2f", taxes);
        System.out.printf("Sales tax (HST):           %10s%n", taxesDsp);
        System.out.println("                           ----------");
        String totMonthlyCharDsp = String.format("$%,.2f",totMonthlyChar);
        System.out.printf("Total monthly charges:     %10s%n", totMonthlyCharDsp);
        String monthlyDuesDsp = String.format("$%,.2f",monthlyDues);
        System.out.printf("Monthly dues:              %10s%n", monthlyDuesDsp);
        System.out.println("                           ----------");
        String totMonthlyFeesDsp = String.format("$%,.2f",totMonthlyFees);
        System.out.printf("Total monthly fees:        %10s%n", totMonthlyFeesDsp);
        String totYearlyFeeDsp = String.format("$%,.2f",totYearlyFee);
        System.out.printf("Total yearly fees:         %10s%n", totYearlyFeeDsp);
        System.out.println();
        String monthlyPayDsp = String.format("$%,.2f",monthlyPay);
        System.out.println("--------------------------------------");
        System.out.printf("Monthly payment:           %10s%n", monthlyPayDsp);
        System.out.println("--------------------------------------");

        System.out.printf("Issued:     %10s%n", ISSUED_DATE);
        System.out.printf("HST Reg No: %21s%n", HST_REG_NO);
        System.out.println();
        String cancelFeeDsp = String.format("$%,.2f", cancelFee);
        System.out.printf("Cancellation fee:          %10s%n", cancelFeeDsp);











    }//End Main
}
