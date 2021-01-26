package baekjoon;

import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int count = 0;
		int len = 0;
		int[] numbers;
		int max = 0;
		int min = 0;
		
		count = in.nextInt();
		len = count;
		numbers = new int[len];
		
		for(int i=0; i<numbers.length; i++) {
			numbers[i] = in.nextInt();
		}
		
		for(int i=0; i<numbers.length; i++) {
			if(i == 0) {
				max = numbers[i];
				min = numbers[i];
			}
			if(max < numbers[i]) {
				max = numbers[i];
			}
			if(min > numbers[i]) {
				min = numbers[i];
			}
		}
		
		System.out.print(min + " " + max);

	}

}
