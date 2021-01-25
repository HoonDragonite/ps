import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[] solution(int[] numbers) {
        int len = numbers.length;
        int[] answer = {};
        int sum = 0;
        
        ArrayList<Integer> answerList = new ArrayList<Integer>();
               
        for(int i=0;i<len-1;i++) {
        	for(int j=1;j<len;j++) {
        		if(i != j) {
        			sum = numbers[i] + numbers[j];
               		if(!answerList.contains(sum)) {
               			answerList.add(sum);
               		}
        		}
           	}
       	}

        Collections.sort(answerList);
        answer = new int[answerList.size()];
        
        for(int i=0; i<answerList.size(); i++) {
        	System.out.println("값 : " + answerList.get(i));
        	answer[i] = answerList.get(i);
        }
        return answer;
    }
}