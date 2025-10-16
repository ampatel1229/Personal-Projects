//todo Javadoc
/**
 * //Homework 5 -- Tower of Hanoi Puzzle
 * This program creates a Tower of Hanoi game where players move disks between three pegs, one at a time, 
 * between three pegs, one at a time, without placing larger disks on top of smaller ones.
 * @author Aman Patel 
 * @version 10/14/2025
 */

public class Disk {
    private int size;
    
    public Disk(int size) {
        this.size = size;
    }
    
    public int getSize() {
        return size;
    }
    
    public String toString() {
        return "Disk[" + size + "]";
    }
}