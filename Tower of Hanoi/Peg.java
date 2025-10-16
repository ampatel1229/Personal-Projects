//todo Javadoc
/**
 * //Homework 5 -- Tower of Hanoi Puzzle
 * This program creates a Tower of Hanoi game where players move disks between three pegs, one at a time, 
 * between three pegs, one at a time, without placing larger disks on top of smaller ones.
 * @author Aman Patel 
 * @version 10/14/2025
 */

public class Peg {
    private Disk[] disks;
    private int count;
    private String name;
    
    public Peg(String name, int capacity) {
        this.name = name;
        disks = new Disk[capacity];
        count = 0;
    }
    
    public String getName() {
        return name;
    }
    
    public int getCount() {
        return count;
    }
    
    public void printPeg() {
        System.out.print("Peg " + name + ":");
        if (count == 0) {
            System.out.println();
            return;
        }
        for (int i = 0; i < count; i++) {
            System.out.print(" " + disks[i]);
            if (i < count - 1) {
                System.out.print(",");
            }
        }
        System.out.println();
        
    }
    
    public boolean addDisk(Disk d) {
        if (count > 0 && disks[count - 1].getSize() < d.getSize()) {
            System.out.println("Invalid move! Cannot place " + d + " on top of " + disks[count - 1] + ".");
            return false;
        }
        disks[count] = d;
        count++;
        return true;
    }
    
    public Disk removeDisk() {
        if (count == 0) {
            System.out.println("Invalid move! Peg " + name + " is empty.");
            return null;
        }
        count--;
        return disks[count];
    }





}