import java.util.ArrayList;

public class Password {
	String website;
	String username;
	String password;
	String info[] = new String[3];
	
	public Password(String website, String username, String password) {
		this.website = website;
		this.username = username;
		this.password = password;
		info[0] = website;
		info[1] = username;
		info[2] = password;
	}
	
	public String getWebsite() {
		return this.website;
	}
	
	public void changeWebstie(String website) {
		this.website = website;
	}
	
	public void changeUsername(String username) {
		this.username = username;
	}
	
	public String getUsername() {
		return this.username;
	}
	
	public String getPassword() {
		return this.password;
	}
	
	public void changePassword(String password) {
		this.password = password;
	}
	
}
