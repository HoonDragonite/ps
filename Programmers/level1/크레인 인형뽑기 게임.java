class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int movesLen = moves.length; //움직일 Count
        int boardHeight = board[0].length; // 
        int boardItem = 0;
        
        int[] bucket = new int[movesLen];
        int bucketIdx = 0;
        
                
        for(int i=0; i<movesLen; i++) {
        	for(int j = 0; j<boardHeight; j++) {
        		boardItem = board[j][moves[i]-1];
        		/*
            	System.out.println("i : " + i);
            	System.out.println("j : " + j);
        		System.out.println("boardItem :" + boardItem);
        		*/
        		if(boardItem != 0) {
        			board[j][moves[i]-1] = 0;
        			if(bucketIdx !=0) {
        				if(bucket[bucketIdx-1] == boardItem) {
        					bucket[bucketIdx-1] = 0;
        					bucketIdx--;
        					answer = answer + 2;
        				}
        				else {
        					bucket[bucketIdx] = boardItem;
        					bucketIdx++;
        				}
        				break;
        			}
        			else {
        				bucket[bucketIdx] = boardItem;
    					bucketIdx++;
    					break;
        			}
        		}
        	}
        }
        return answer;
    }
}
