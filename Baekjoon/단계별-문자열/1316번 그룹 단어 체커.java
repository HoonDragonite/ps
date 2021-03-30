package ps;

import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int wordCount = 0;
		int groupWordCount = 0;
		String[] words;
		boolean isGroupWord = false;
		ArrayList<Character> alphabetList = new ArrayList<Character>();
		
		wordCount = in.nextInt();
		words = new String[wordCount];
		
		for(int i=0; i<wordCount; i++) {
			words[i] = in.next();
		}
		
		for(int i=0; i<words.length; i++) {
			for(int j=0; j<words[i].length(); j++) {
				if(j == 0) {
					alphabetList.add(words[i].charAt(j));
				}
				if(j != 0 && words[i].charAt(j-1) != words[i].charAt(j)) {
					if(alphabetList.contains(words[i].charAt(j)) == true) {
						isGroupWord = false;
						break;
					}
					else {
						alphabetList.add(words[i].charAt(j));
					}
				}
				
				isGroupWord = true;
			}
			if(isGroupWord == true) {
				groupWordCount++;
			}
			alphabetList.clear();
		}

		System.out.println(groupWordCount);
	}
}