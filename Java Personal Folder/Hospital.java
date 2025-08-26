import java.util.Scanner;

class Patient {
    
    String name;
    int age;
    Dob pdob;
    
    
    void display (){
        System.out.println("Name:" +name);
        System.out.println("Age:" +age);
        System.out.println("DOB ");
        pdob.dobDisplay();
        
    }
    
    class Dob {
        int month;
        int day;
        int year;
        
        void dobDisplay(){
            System.out.print(month+"/"+day+"/"+year);
            System.out.println();
        }
    }
    
}

class Room {
    int roomNum;
    int type;
    String rType="";
    
    void determineType(int type) {
    if (type==1) {
        rType ="Airconditioned";
    }
    else {
        rType="Regular";
    }
   }
    
    void rDisplay(){
        System.out.println("Room: "+roomNum);
        System.out.println("Room Type: "+rType);
    }
}

public class Hospital
{
    
	public static void main(String[] args) {
	    
	    Scanner scan = new Scanner(System.in);
	    
	    Patient p1 = new Patient();
	    Patient.Dob b1 = p1.new Dob();
	    Room r1 = new Room();
		
		
		System.out.print("Enter Name: ");
		p1.name = scan.nextLine();
		System.out.print("Enter Age: ");
		p1.age = scan.nextInt();
		scan.nextLine();
		
		System.out.println("---------------");
		System.out.print("DOB \nMonth:");
		b1.month = scan.nextInt();
		
		System.out.print("Day:");
		b1.day = scan.nextInt();
		System.out.print("year:");
		b1.year = scan.nextInt();
		p1.pdob =b1;
		scan.nextLine();
		
		System.out.println();
	    System.out.println("Enter Room Details");
		System.out.print("Enter Room Number: ");
		r1.roomNum = scan.nextInt();
		scan.nextLine();
		
		System.out.println("Enter Room Type (1 - Airconditioned | 2 - Regular): ");
		System.out.print("Type: ");
		r1.type = scan.nextInt();
		
		r1.determineType(r1.type);
		
		System.out.println();
		System.out.println("---------------");
		System.out.println("Patient Details");
		
		
		p1.display();
		r1.rDisplay();
		
		
		
		
		
		
		
		
		
	}
}