package ps;

import java.util.*;

public class Main {
	
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		int alphabet[] = new int[26];
		String word = "";
		
		word = in.next();
		
		for(int i=0; i<alphabet.length; i++) {
			alphabet[i] = -1;
		}
		
		for(int i=0; i<word.length(); i++) {
			if(alphabet[word.charAt(i)-97] != -1) {
				continue;
			}
			alphabet[word.charAt(i)-97] = i;
		}
		
		for(int i=0; i<alphabet.length; i++) {
			System.out.print(alphabet[i] + " ");
		}
		
	}
}
