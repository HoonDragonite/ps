package baekjoon;

import java.util.*;



public class Test {
	long sum(int[] a) {
        long ans = 0;
        int len = 0;
		len = a.length;
		
		for(int i=0; i<len; i++) {
			ans = ans + a[i];
		}
        return ans;
    }
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
	
	}

}