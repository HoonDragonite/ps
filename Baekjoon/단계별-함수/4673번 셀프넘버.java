package ps;

import java.util.*;

/*
	시간복잡도 : O(2n)
*/

public class Main {
	
	public static int selfNumber(int number) {
		int selfNumber = 0;
		int n = 0;
		
		selfNumber = selfNumber + number;
		
		while(true) {
			n = number % 10;
			number = number / 10;
			selfNumber = selfNumber + n;
			if (number == 0) {
				break;
			}
		}

		return selfNumber;
	}
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int[] numbers = new int[10001];
		
		for(int i=1; i<numbers.length; i++) {
			if(selfNumber(i) < 10001) {
				numbers[selfNumber(i)] = 1;
			}
		}
		
		for(int i=1; i<numbers.length; i++) {
			if(numbers[i] != 1) {
				System.out.println(i);
			}
		}
	}
}
