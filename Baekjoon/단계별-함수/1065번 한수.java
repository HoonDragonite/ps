package baekjoon;

import java.util.*;

public class Main {
	public static int CountingHanSoo(int num) {
		int count = 0;
		int num100 = 0;
		int num10 = 0;
		int num1 = 0;
		int number = 0;
		
		if(num < 100) {
			return num;
		}
		else {
			count = count + 99;
			for(int i=100; i <= num; i++) {
				number = i;
				num100 = number/100;
				number = number%100;
				num10 = number/10;
				num1 = number%10;
				if((num100 - num10) == (num10 - num1)) {
					count++;
				}
			}
		}
		
		return count;
	}
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n;
        n = in.nextInt();
		System.out.println(CountingHanSoo(n));
	}

}
