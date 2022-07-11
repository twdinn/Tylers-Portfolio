// Program to Calculate Rental Bill
// Written By: Tyler Dinn
// Date: March 22 2022

import java.util.Scanner;

public class CarRentalCompany {
    public static void main(String[] args) {
        // Program Constants
        final double PER_DAY_CHAR = 35.00;
        final double PER_KILO_CHAR = 0.10;
        final double HST_RATE = 0.15;

        // Data Entered By User
        String custName;
        String phoneNum;
        int numDays;
        int rentMil;
        int returnMil;

        Scanner keyboard = new Scanner(System.in);

        System.out.print("Enter Customer Name: ");
        custName = keyboard.nextLine();
        System.out.print("Enter Customer Phone Number: ");
        phoneNum = keyboard.nextLine();
        System.out.print("Enter Number of Days the Car Was Rented: ");
        numDays = keyboard.nextInt();
        System.out.print("Enter the Mileage When the Car Was Rented: ");
        rentMil = keyboard.nextInt();
        System.out.print("Enter the Mileage When the Car Was Returned: ");
        returnMil = keyboard.nextInt();

        // Calculations for the Program
        int kiloTravel = returnMil - rentMil;
        double dailyCost = PER_DAY_CHAR * numDays;
        double mileCost = PER_KILO_CHAR * kiloTravel;
        double rentCost = dailyCost + mileCost;
        double hst = dailyCost * HST_RATE;
        double totalRentCost = rentCost + hst;

        // Display Outputs and Calculations
        System.out.println();
        System.out.println("Customer Name:                      "   + custName);
        System.out.println("Customer Phone Number:              "   + phoneNum);
        System.out.println("Number of Days the Car Was Rented:  "   + numDays);
        System.out.println("Mileage When the Car Was Rented:    "   + rentMil);
        System.out.println("Mileage When the Car Was Returned   "   + returnMil);
        System.out.println();
        System.out.println("Number of kilometers traveled:      "   + kiloTravel);
        System.out.println("Cost for the Rental:               $"   + rentCost);
        System.out.println("HST:                               $"   + hst);
        System.out.println("Total Rental Cost:                 $"   + totalRentCost);



    }//End Main

}
