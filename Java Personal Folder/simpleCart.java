
//Simple Billing
import java.util.Scanner;

public class simpleCart {

    // Display the main welcome menu
    public static void welcome() {
        System.out.println("===============================================");
        System.out.println("                    Welcome                    ");
        System.out.println("===============================================");
        System.out.println("Item                               Price");
        System.out.println("_____________________________________________");
        System.out.println("1. Potion             ----             5");
        System.out.println("2. Elixir             ----            10");
        System.out.println("3. Homing warp Totem  ----            13");
        System.out.println("4. Exit\n");
    }

    // Calculate total price
    public static int calculateTotal(int psum, int esum, int tsum) {
        return psum + esum + tsum;
    }

    // Checkout method that returns true or false based on payment success
    public static boolean checkout(int pquantity, int equantity, int tquantity, Scanner scan, int psum, int esum, int tsum) {
        int bill = psum + esum + tsum;

        System.out.println("\n----------- Bill Receipt ----------");
        System.out.println("Potion QTY: " + pquantity + " x 5");
        System.out.println("Elixir QTY: " + equantity + " x 10");
        System.out.println("Totem QTY: " + tquantity + " x 13");
        System.out.println("Total Bill: " + bill);

        // Payment process
        while (true) {
            System.out.print("Enter Payment: ");
            int payment = scan.nextInt();

            if (payment < bill) {
                System.out.println("Insufficient funds! Please pay the amount due.");
                System.out.println("1. Retry Payment\n2. Return to Shopping");
                int choice = scan.nextInt();
                if (choice == 2) {
                    return false; // Returning false if the user opts to return to shopping
                }
            } else {
                int change = payment - bill;
                System.out.println("Change: " + change);
                System.out.println("Thank you for purchasing!");
                return true; // Returning true if the payment is successful
            }
        }
    }

    public static void main(String[] args) {
        int psum = 0, esum = 0, tsum = 0;
        int pquantity = 0, equantity = 0, tquantity = 0;

        Scanner scan = new Scanner(System.in);

        while (true) {
            welcome();
            System.out.print("Navigate using number 1-4: ");
            int choice = scan.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter quantity: ");
                    int pq = scan.nextInt();
                    pquantity += pq;
                    psum += pq * 5;
                    break;

                case 2:
                    System.out.print("Enter quantity: ");
                    int eq = scan.nextInt();
                    equantity += eq;
                    esum += eq * 10;
                    break;

                case 3:
                    System.out.print("Enter quantity: ");
                    int tq = scan.nextInt();
                    tquantity += tq;
                    tsum += tq * 13;
                    break;

                case 4:
                    // Exit option
                    System.out.println("Thank you for visiting! Exiting...");
                    scan.close();
                    return;

                default:
                    System.out.println("Invalid choice, please try again.");
                    continue;
            }

            System.out.println("\n1. Checkout\n2. Continue shopping");
            int nextChoice = scan.nextInt();
            if (nextChoice == 1) {
                int total = calculateTotal(psum, esum, tsum);
                boolean checkoutSuccessful = checkout(pquantity, equantity, tquantity, scan, psum, esum, tsum);
                
                if (checkoutSuccessful) {
                    System.out.println("\nThank you for your purchase!");
                    break; // Exit after successful purchase
                } else {
                    System.out.println("\nReturning to shopping...");
                    continue; // Return to shopping if payment fails
                }
            }
        }

        scan.close();
    }
}