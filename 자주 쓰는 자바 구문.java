// ******************* 자료구조 *******************

// ArrayList
List<String> strList = ArrayList<String>();

// Map
Map<String, String> map = new HashMap<>();

// Set
HashSet<String> hs01 = new HashSet<String>();

// BST
TreeSet<Integer> ts = new TreeSet<Integer>();

//Stack
Stack<Integer> st = new Stack<Integer>();

//Queue
LinkedList<String> qu = new LinkedList<String>();

// Heap
PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(); //Min heap
PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder()); //Max heap


// ******************* 자주 쓰는 *******************
    // 리스트의 최댓값 최솟값
    int maxValue = Collections.max(list);
    int minValue = Collections.min(list);

// ******************* 입력 받기 *******************

// 단순 문자열 입력

    // 공백으로 구분하여 변수에 입력받기

    //

    // 공백으로 구분하여 숫자 리스트에 입력받기
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    ArrayList<Integer> datas = new ArrayList<>();

    while(st.hasMoreTokens()) { 
        datas.add(Integer.parseInt(st.nextToken()));
    }
    
    for(int d : datas) {
        System.out.println(d);
    }  

    // 공백으로 구분하여 문자열 리스트에 입력받기
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    ArrayList<String> datas = new ArrayList<>();

    while(st.hasMoreTokens()) { 
        datas.add(st.nextToken());
    }
    
    for(String data : datas) {
        System.out.println(data);
    }

// 연속된 숫자를 숫자단위 배열로 입력받기 (숫자그래프)
// 연속된 문자를 문자단위 배열로 입력받기 (문자그래프)
// 한 줄에는 수의 개수 n 가 주어지고, 다음에는 n개의 수가 주어진다

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

// 행렬 변환하기

// ******************* 문자열 관련 *******************

// 문자열 비교
Bool b = "is".equals("is");

// 문자열 분리 -> split, StringTokenizer

// 문자열 자르기
String a = "abcde";
String subA = a.substring(2,3); // 인덱스 2~3


// 문자열 반대로 출력
StringBuffer sb = new StringBuffer(str);
sb.reverse();


// ******************* 배열 관련 *******************
// 오름차순 정렬
int[] nums2 = {1, 3, 4, 2, 5};
Arrays.sort(nums2);

// 내림차순 정렬
Arrays.sort(nums2, Collections.reverseOrder());

// 배열의 특정원소 모두 지우기

// 배열 중복제거

// 배열 슬라이싱
Arrays.copyOfRange(nums2, 2, 3);

// ******************* 순회 관련 *******************

// 배열 순회 : count만큼
int count = 10;
for(int i=0; i<count; i++){

}

// 배열 순회 : 배열의 길이만큼
int len = 5;
int[] nums = new int[5];

for(int i=0; i<nums.length; i++){

}

// 배열의 원소 순회
for(int i : nums){
    
}

// 리스트 순회
for (Iterator<Pair> it = list.iterator(); it.hasNext();) {
    Pair p = it.next();
    if(p.a == 5)
    	it.remove();
}


/////////////////// Math 관련 ////////////////////


// 절대값

// 반올림 관련, 소숫점 n번째 자리
double e = 2.71859;
System.out.println(Math.round(e)); // 정수로 만들기
System.out.println(Math.round(e*100)/100.0); // 1번째 자리까지
System.out.println(Math.round(e*10)/10.0); // 2번째 자리까지

// 지수 계산
System.out.println(Math.pow(3, 2)); // 3\*\*2

// 난수 뽑기
System.out.println(Math.random()); // 0.0 ~ 1.0 사이

// 자릿수의 합
