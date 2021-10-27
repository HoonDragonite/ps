import java.io.*;
import java.util.*;
import java.math.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int data = Integer.parseInt(br.readLine());
		
		System.out.println(fibonacci(data));
	}

	public static int fibonacci(int num) {
		if (num < 2) {
			return num;
		}
		
		return fibonacci(num-1) + fibonacci(num-2);
	}
}