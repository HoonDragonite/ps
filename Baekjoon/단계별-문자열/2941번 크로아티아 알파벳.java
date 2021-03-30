package ps;

import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String word = "";
		int count = 0;
		String[] croatiaAlphabets = {"c=","c-","dz=","d-","lj","nj","s=","z="};

		word = in.nextLine().trim();
		
		for(int i=0; i<croatiaAlphabets.length; i++) {
			if(word.contains(croatiaAlphabets[i])) {
				word = word.replaceAll(croatiaAlphabets[i], " ");
			}
		}
		
		System.out.println(word.length());
	}
}