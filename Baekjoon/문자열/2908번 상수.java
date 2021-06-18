package ps;

import java.util.*;
/*
    키워드 : 문자열 뒤집기, StringBuffer
*/
public class Main {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int num1 = 0;
		int num2 = 0;
		String strNum1 = "";
		String strNum2 = "";
		StringBuffer stringBuffer = new StringBuffer();
		
		num1 = in.nextInt();
		num2 = in.nextInt();
		
		strNum1 = Integer.toString(num1);
		strNum2 = Integer.toString(num2);
		
		stringBuffer.append(strNum1);
		strNum1 = stringBuffer.reverse().toString();
		
		stringBuffer.delete(0,stringBuffer.length());

		stringBuffer.append(strNum2);
		strNum2 = stringBuffer.reverse().toString();
		
		num1 = Integer.parseInt(strNum1);
		num2 = Integer.parseInt(strNum2);
		
		if(num1 > num2) {
			System.out.println(num1);
		}
		else if(num1 < num2){
			System.out.println(num2);
		}
	}
}