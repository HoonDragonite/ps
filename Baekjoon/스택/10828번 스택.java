package baekjoon;

import java.io.*;
import java.util.*;


import java.math.*;

public class Main {

	static List<Integer> myStack = new ArrayList<>();
	
	public static void push(int data) {
		myStack.add(data);
	}
	
	public static int pop() {
		if(myStack.size() == 0) {
			return -1;
		}
		
		return myStack.remove(myStack.size()-1);
	}
	
	public static int size() {
		return myStack.size();
	}
	
	public static int empty() {
		return myStack.size() == 0 ? 1 : 0;
	}
	
	public static int top() {
		return myStack.size() == 0 ? -1 : myStack.get(myStack.size()-1);
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int orderCount = Integer.parseInt(br.readLine());
	
		for(int i=0; i<orderCount; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			switch(st.nextToken()){
				case "push":
					int num = Integer.parseInt(st.nextToken());
					push(num);
					break;
				case "pop":
					System.out.println(pop());
					break;
				case "size":
					System.out.println(size());
					break;
				case "empty":
					System.out.println(empty());
					break;
				case "top":
					System.out.println(top());
					break;
			}
		}
	}
}