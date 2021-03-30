import java.util.*;

/*
	키워드 : 아스키코드, 대소문자 구분안함
*/

public class Main {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String word = "";
		int max = 0;
		char result = ' ';
		int[] wordCount = new int[26];
		
		word = in.next();
				
		word = word.toUpperCase();
		
		for(int i=0; i<wordCount.length; i++) {
			wordCount[i] = 0;
		}
		
		for(int i=0; i<word.length(); i++) {
			wordCount[word.charAt(i) - 65]++;
		}
		
		for(int i=0; i<wordCount.length; i++) {
			if(max == wordCount[i]) {
				max = wordCount[i];
				result = '?';
			}
			else if(max < wordCount[i]) {
				max = wordCount[i];
				result = (char) (i+65);
			}
		}
		
		System.out.println(result);
	}
}