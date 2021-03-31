// 기본 양식
import java.util.*;

class Main{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
    }
}


// 배열 순회1 정해진 수만큼
int count = 10;
for(int i=0; i<count; i++){

}

// 배열 순회2
int len = 5;
int[] nums = new int[5];

for(int i=0; i<nums.length; i++){
    
}

// 배열 원소 순회
for(int i : nums){

}

// 오름차순 정렬
int[] nums2 = {1, 3, 4, 2, 5};
Arrays.sort(nums2);

// 내림차순 정렬
Arrays.sort(nums2, Collections.reverseOrder());

// n개의 0으로 채워진 배열 만들기
int[] nums3 = new int[len];

// n x m 행렬 리스트로 만들기
int n = 4;
int m = 4;
int[][] twoDivMatrix = new int[n][m];

for(int i=0; i<n; i++) {
    for(int j=0; j<m; j++) {
        System.out.print(twoDivMatrix[i][j] + " ");
    }
    System.out.println();
}

// 반올림 관련, 소숫점 n번째 자리
double e = 2.71859;
System.out.println(Math.round(e)); // 정수로 만들기
System.out.println(Math.round(e*100)/100.0); // 1번째 자리까지
System.out.println(Math.round(e*10)/10.0); // 2번째 자리까지

// 지수 계산
System.out.println(Math.pow(3, 2)); // 3**2

// 난수 뽑기
System.out.println(Math.random()); // 0.0 ~ 1.0 사이