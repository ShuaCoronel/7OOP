import java.util.Scanner;

public class GradeCalculator {
    public static void main(String args[]) {
        String name;
        int[] scores = new int[3];
        double average;
        Scanner userIn = new Scanner(System.in);

        while (true) {
            System.out.println("Enter Student name: (or type 'exit' to stop)");
            name = userIn.nextLine();

            if (name.equalsIgnoreCase("exit")) {
                System.out.println("Program terminated.");
                break;
            }

            for (int i = 0; i < 3; i++) {
                System.out.println("Enter Exam score " + (i + 1) + ":");
                scores[i] = userIn.nextInt();
                userIn.nextLine();
            }
            
            System.out.println();
            average = average(name, scores);
            System.out.println();
        }
    }

    public static double average(String name, int[] score) {
        int sum = 0;
        for (int i = 0; i < 3; i++) {
            sum += score[i];
        }

        double average = (double) sum / 3;

        System.out.println("Name: " + name);
        System.out.print("Scores: ");
        for (int i = 0; i < 3; i++) {
            System.out.print(score[i] + " ");
        }
        System.out.println();
        System.out.printf("Average: %.2f%n", average);

        if (average >= 90) {
            System.out.println("Grade: A");
        } else if (average < 90 && average >= 80) {
            System.out.println("Grade: B");
        } else if (average < 80 && average >= 70) {
            System.out.println("Grade: C");
        } else if (average < 70 && average >= 60) {
            System.out.println("Grade: D");
        } else {
            System.out.println("Grade: F");
        }

        return average;
 }
 }