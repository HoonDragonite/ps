import java.util.*;

/*
    관계는 참가자 그룹에 완주자가 포함되어 있는 형태
    해쉬 맵 하나에 참가자 이름으로 키를 구성하고 값에는 Counting을 실시한다.
    시간복잡도 : O(n)
*/

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        HashMap<String, Integer> hashMap = new HashMap<String, Integer>();
        
        for(String name : participant) {
        	hashMap.put(name, hashMap.getOrDefault(name, 0) + 1);
        }
        
        for(String name : completion) {
        	hashMap.put(name, hashMap.get(name) - 1);
        }
                
        for(String name : hashMap.keySet()) {
        	if(hashMap.get(name) != 0) {
        		answer = name;
        	}
        }
        
        return answer;
    }
}


/* 원래 푼 풀이

시간복잡도 : O(n^2)

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        for(int i=0; i<participant.length; i++){
            for(int j=0; j<completion.length; j++){
            	if(participant[i].equals(completion[j])) {
                    //System.out.println(participant[i]);
                    //System.out.println(completion[j]);
                    participant[i] = "";
                    completion[j] = "";
            		break;
            	}
            }
        }
        
        for(int i=0; i<participant.length; i++){
            if(participant[i] != "") {
        		answer = participant[i];
        	}
        }
        
        return answer;
    }
}

*/
