package baekjoon;

import java.io.*;
import java.util.*;


import java.math.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		   
		int count = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] numList = new int[st.countTokens()];
		int i = 0;
		while(st.hasMoreTokens()) {
			numList[i++] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(numList);
		
		System.out.println(numList[0] + " " + numList[numList.length - 1]);	
	}
}