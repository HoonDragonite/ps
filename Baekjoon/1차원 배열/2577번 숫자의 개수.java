import java.util.*;

public class Main {
	public static void main(String[] args) {
		int num1 = 0;
		int num2 = 0;
		int num3 = 0;
		int[] numbers = new int[10];
		int sum = 0;
		int item = 0;
		
		Scanner in = new Scanner(System.in);
		
		num1 = in.nextInt();
		num2 = in.nextInt();
		num3 = in.nextInt();
		
		sum = num1 * num2 * num3;
		
		while(true) {
			if(sum == 0) {
				break;
			}
			item = sum % 10;
			numbers[item]++;
			
			sum = sum/10;
		}
		
		for(int i=0; i<numbers.length; i++) {
			System.out.println(numbers[i]);
		}
	}
}