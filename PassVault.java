import java.util.*;

public class PassVault {

	public static void main(String[] args) {
		//variable needed to exit while loop
		String exit = "x";
		
		//create Scanner
		Scanner input = new Scanner(System.in);
		input.useDelimiter("\\s*");
		//Create variables needed for the account
		Account myAccount = new Account();
		String website = "";
		String username = "";
		String password = "";
		System.out.println("Enter the website, username, and password you want saved: ");
		while (!exit.equals("q")) {
			System.out.print("Website: ");
			website = input.nextLine();
			System.out.print("Username: ");
			username = input.nextLine();
			System.out.print("Password: ");
			password = input.nextLine();
			Password pass = new Password(website, username, password);
			myAccount.vault.add(pass.info);
			System.out.println("Enter q if your are done entering information");
			exit = input.nextLine();
			System.out.println();
		}
		input.close();


		myAccount.printInfo();
	}
}
