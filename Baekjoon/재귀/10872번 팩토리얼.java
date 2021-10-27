package baekjoon;

import java.io.*;
import java.util.*;
import java.math.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int data = Integer.parseInt(br.readLine());
		
		System.out.println(factorial(data));
	}

	public static int factorial(int num) {
		if (num <= 1) {
			return 1;
		}
		return (num)*factorial(num-1);
	}
}