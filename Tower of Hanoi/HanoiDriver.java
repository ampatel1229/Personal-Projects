import java.util.Scanner;

//todo Javadoc
/**
 * //Homework 5 -- Tower of Hanoi Puzzle
 * This program creates a Tower of Hanoi game where players move disks between three pegs, one at a time, 
 * between three pegs, one at a time, without placing larger disks on top of smaller ones.
 * @author Aman Patel 
 * @version 10/14/2025
 */


public class HanoiDriver {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Welcome to Tower of Hanoi!");
        System.out.println("Enter number of disks:");
        int numDisks = input.nextInt();

        HanoiGame game = new HanoiGame(numDisks);
        
        System.out.println("\nInitial State:");
        game.printBoard();
        System.out.println();
        
        boolean first = true;
        
        while (!game.isSolved()) {
            System.out.println("\nEnter your move(from to): ");
            String from = input.next();
            String to = input.next();
            
            boolean success = game.moveDisk(from, to);
            
            if (!success) {
                if (first) {
                    System.out.println("Initial State:");
                    first = false;
                }
                game.printBoard();
                continue;
            }
            
            first = false;
            game.printBoard();
        }
        System.out.println("\nCongratulations! You solved Tower of Hanoi in " + game.getMoves() + " moves!"); 
    }
}
