import java.io.*;
import java.util.*;
import java.math.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int count = Integer.parseInt(br.readLine());
		
		for (int i=0; i<count; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int multiCount = Integer.parseInt(st.nextToken());
			String str = st.nextToken();
			
			for(int j=0; j<str.length(); j++) {
				for(int k=0; k<multiCount; k++) {
					System.out.print(str.charAt(j));
				}
			}
			System.out.println();
		}
		
	}
}