package baekjoon;

import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		float max = 0;
		int count = 0;
		float numbers[];
		float sum = 0;
		
		count = in.nextInt();
		numbers = new float[count];
		
		max = numbers[0];
		
		for(int i=0; i<numbers.length;i++) {
			numbers[i] = in.nextInt();
			if(max < numbers[i]) {
				max = numbers[i];
			}
		}
		
		for(int i=0;i<numbers.length;i++) {
			numbers[i] = numbers[i]/max *100;
			sum += numbers[i];
		}
		
		System.out.print(sum/count);
	}

}
