//todo Javadoc
/**
 * //Homework 5 -- Tower of Hanoi Puzzle
 * This program creates a Tower of Hanoi game where players move disks between three pegs, one at a time, 
 * between three pegs, one at a time, without placing larger disks on top of smaller ones.
 * @author Aman Patel 
 * @version 10/14/2025
 */

public class HanoiGame {
    private Peg[] pegs;
    private int numDisks;
    private int moves;
    
    public HanoiGame(int numDisks) {
        this.numDisks = numDisks;
        pegs = new Peg[3];
        pegs[0] = new Peg("A", numDisks);
        pegs[1] = new Peg("B", numDisks);
        pegs[2] = new Peg("C", numDisks);
        moves = 0;
        for (int i = numDisks; i >= 1; i--) {
            pegs[0].addDisk(new Disk(i));
        }
    }
    
    public boolean moveDisk(String from, String to) {
        Peg source = getPeg(from);
        Peg dest = getPeg(to);
        
        if (source == null || dest == null) {
            System.out.println("Invalid peg name. Use A, B, or C.");
            return false;
        }
        
        if (source.getCount() == 0) {
            System.out.println("Invalid move! Peg " + from + " is empty.");
            return false;
        }
        
        Disk moving = source.removeDisk();
        
        boolean place = true;
        Disk temp = null;
        
        if (dest.getCount() > 0) {
            temp = dest.removeDisk();
            dest.addDisk(temp);
            if (moving.getSize() > temp.getSize()) {
                place = false;
            }
        }
        
        if (!place) {
            System.out.println("Invalid move! Cannot place " + moving + " on top of " + temp + ".");
            source.addDisk(moving);
            return false;
        }
        
        dest.addDisk(moving);
        moves++;
        System.out.println("Moved " + moving + " from " + from + " to " + to + ".");
        return true;
    }
    
    public Peg getPeg(String name) {
        for (Peg p : pegs) {
            if (p.getName().equals(name)) {
                return p;
            }
        }
        return null;
    }
    
    public boolean isSolved() {
        return (pegs[1].getCount() == numDisks || pegs[2].getCount() == numDisks);
    }
    
    public void printBoard() {
        for (Peg p : pegs) {
            p.printPeg();
        }
    }
    
    public int getMoves() {
        return moves;
    }
}