import java.util.*;

/*
	총 비용 = A + B * D
	판매 비용 = C * D
	판매 비용 > 총 비용이 되는 수량 D를 구하라
	
	A + B * D > C * D
	
	(A + B * D) - (C * D) > 0
	
	1차함수니까 언젠간 만나겠지 차이가 줄여지면서
	수량을 늘려갈 때 n + 1회차의 (판매 비용 - 총 비용)이 n회차의 (판매 비용 - 총 비용)보다 작아야 한다.
	n회차의 (판매 비용 - 총 비용) <= n+1회차의 (판매 비용 - 총 비용)이면 -1을 리턴한다.
	
*/


/*

시간 초과로 뜬 코드. 다시 풀기

public class Main {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		long fixedAmt = 0;    // 고정비 A
		long changedAmt = 0; // 가변비 B
		long price = 0; // 가격 C
		long qty = 0; // 수량 D
		long totAmt = 0; // 총 비용 A + B*D
		long saleAmt = 0; // 판매비용 C*D
		long nextQty = 0;
		long nextTotAmt = 0;
		long nextSaleAmt = 0;
		
		
		fixedAmt = in.nextInt(); 
		changedAmt = in.nextInt();
		price = in.nextInt();
		
		while(true) {
			qty = qty + 1;
			totAmt = fixedAmt + (changedAmt * qty);
			saleAmt = price * qty;
			
			nextQty = qty + 1;
			nextTotAmt = fixedAmt + (changedAmt * nextQty);
			nextSaleAmt = price * nextQty;
			
			if((totAmt - saleAmt) <= (nextTotAmt - nextSaleAmt)) {
				System.out.println(-1);
				break;
			}
			else {
				if(saleAmt > totAmt) {
					System.out.println(qty);
					break;
				}
			}
			
		}
	}
}

*/