/*
 * CSCI3180 Principles of Programming Languages
 *
 * --- Declaration ---
 *
 * I declare that the assignment here submitted is original except for source
 * material explicitly acknowledged. I also acknowledge that I am aware of
 * University policy and regulations on honesty in academic work, and of the
 * disciplinary guidelines and procedures applicable to breaches of such policy
 * and regulations, as contained in the website
 * http://www.cuhk.edu.hk/policy/academichonesty/
 *
 * Assignment 2
 * Name : Huzeyfe Kiran
 * Student ID : 1155104019
 * Email Addr : 1155104019@link.cuhk.edu.hk
 */
public class Potion extends NPC{
    
    private static final int AMOUNT_CAP = 20;
    private int amount;
  
	public Potion(int posx, int posy, int index, Map map) {
		super(posx, posy, index, map);
		this.setName("P" + Integer.toString(index));
		this.setAmount(TheJourney.rand.nextInt(AMOUNT_CAP - 5) + 5);
	}
 
    public boolean actionOnWarrior(Warrior warrior) {
		warrior.increaseHealth(this.getAmount());
		warrior.talk("Very good, I got additional healing potion "+ this.getName()+".");
        warrior.getMap().setLand(warrior.getPos(), null);
        warrior.setPos(this.getPos());
        warrior.getMap().setLand(warrior.getPos(), warrior);
        this.setPos(null);
        this.map.deleteTeleportableObj(this);
    	return false;
    }

    public void teleport(){
        Pos p = this.map.getUnOccupiedPosition();
        this.map.setLand(this.getPos(), null);
        this.setPos(p);
        this.map.setLand(this.getPos(), this);
    }

    public void setAmount(int amount){
        this.amount = amount;
    }

    public int getAmount(){
        return this.amount;
    }
}
