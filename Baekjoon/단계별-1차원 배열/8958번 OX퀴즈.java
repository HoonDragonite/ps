import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int len = 0;
		int oCount = 0;
		int xCount = 0;
		int score = 0;
		int point = 0;
		
		len = in.nextInt();
		
		String[] str = new String[len];
		
		for(int i=0; i<str.length; i++) {
			str[i] = in.next();
		}
		
		for(int i=0; i<str.length; i++) {
			score = 0;
			point = 0;
			for(int j=0; j<str[i].length();j++) {
				if(str[i].charAt(j) == 'O') {
					point++;
					score = score + point;
				}
				else {
					point = 0;
				}
			}
			System.out.println(score);
		}
	}
}