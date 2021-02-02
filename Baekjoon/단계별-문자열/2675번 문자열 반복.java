import java.util.*;

/*
	키워드 : 반복문 잘 쓰기
*/

public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		String[] words;
		int wordCount = 0;
		int repeat[];
		
		wordCount = in.nextInt();
		words = new String[wordCount];
		repeat = new int[wordCount];
		
		for(int i=0; i<wordCount; i++) {
			repeat[i] = in.nextInt();
			words[i] = in.next();
		}
		
		for(int i=0; i<wordCount; i++) {
			for(int j=0; j<words[i].length(); j++) {
				for(int k=0; k<repeat[i]; k++) {
					System.out.print(words[i].charAt(j));
				}
			}	
			System.out.println();
		}
	}
}
