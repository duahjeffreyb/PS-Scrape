import java.util.*;
public class Account {
	ArrayList<String[]> vault = new ArrayList<String[]>();

	public Account() {
		
	}
	
	public Account(String[] info) {
		vault.add(info);
	}
	
	public void printInfo() {
		for(String[] info: vault) {
			System.out.println("Website: " + info[0]);
			System.out.println("Username: " + info[1]);
			System.out.println("Password: " + info[2]);
			System.out.println();
		}
	}
	
}
