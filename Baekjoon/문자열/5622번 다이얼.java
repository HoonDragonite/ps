package ps;

import java.util.*;

public class Main {
	
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String callNo = "";
		char idxChar = ' ';
		int toltalTime = 0;
		
		callNo = in.next();
		
		for(int i=0; i<callNo.length(); i++) {
			idxChar = callNo.charAt(i);
			toltalTime = toltalTime + 2; 
			
			if((int)idxChar >= 65) { 
				toltalTime++;
			}
			if((int)idxChar >= 68) {
				toltalTime++;
			}
			if((int)idxChar >= 71) {
				toltalTime++;
			}
			if((int)idxChar >= 74) {
				toltalTime++;
			}
			if((int)idxChar >= 77) {
				toltalTime++;
			}
			if((int)idxChar >= 80) {
				toltalTime++;
			}
			if((int)idxChar >= 84) {
				toltalTime++;
			}
			if((int)idxChar >= 87) {
				toltalTime++;
			}
		}
		System.out.println(toltalTime);
	}
}