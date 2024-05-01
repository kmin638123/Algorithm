# Algorithm Study

## 파이썬 기본
1. __문자열__ 함수
> - s.find(x, start, end): start, end 사이 범위에서 x가 존재한다면 해당 위치의 index를 반환하고, 존재하지 않는다면 -1을 반환!
> - s.count(x, start, end): start, end 사이 범위에서 x가 존재한다면 x의 개수를 반환하고, 존재하지 않는다면 0을 반환!
2. __lambda__ 함수: lambda argument: expression (인자는 ,로 구분!)
> - __map__ 함수와 함께 사용: 리스트(or 튜플)의 각 요소에 lambda expression 적용하고 싶을 때
>    * mylist2 = list(map(lambda x: x*2, mylist))
> - __filter__ 함수와 함께 사용: 리스트(or 튜플)에 대해 lambda expression에 맞는 요소만 추출하고 싶을 때
>    * mylist2 = list(filter(lambda x: x%2==1, mylist))
> - __sorted__ 함수와 함께 사용: 리스트(or 튜플)에 대해 lambda expression의 기준으로 정렬하고 싶을 때
>    * mylist2 = sorted(mylist, key = lambda x: (len(x), x)) 
3. __2차원 리스트__ (세로 n, 가로 m: n x m)
> - array = [[0] * m for _ in range(n)]
4. __반복문 제어__ 하기
>- __pass__: 실행할 코드가 없는 것으로 바로 다음 코드 실행
> - __continue__: 반복문 내의 다음 코드를 실행하지 않고, 바로 다음 순서의 loop을 실행
> - __break__: 반복문을 멈추고, loop 밖으로 나감


## 파이썬 라이브러리
1. __sys__: import sys
>- sys.stdin.readline()
>- sys.setrecursionlimit(10 ** 6)
>    * 재귀 사용 문제에서 필수!  
>    * 파이썬 기본 재귀 깊이 제한 = 1000
2. __itertools__: from itertools  import ~
> - list(permutations(data, a)): 순열 (a개 뽑아 나열)
> - list(combinations(data, b)): 조합 (b개 뽑아 순서없이 나열)
> - list(product(data, repeat=c)): 중복 순열 (총 c개 뽑아 나열)
> - list(combinations_with_replacement(data, d)): 중복 조합
3. __heapq__: import heapq
> - heapq.heappush(h, value) || heapq.heappush(h, -value)
> - heapq.heappop(h) || -heapq.heappop(h)
4. __bisect__: from bisect import ~
> - bisect.bisect_left(seq, x, lo=0, hi=None): 정렬된 seq 내에서 x가 삽입되어야 할 가장 왼쪽 인덱스 반환
>    * lo, hi는 탐색 범위를 지정하는 인덱스, 보통은 생략
> - bisect.bisect_right(seq, x, lo=0, hi=None): 정렬된 seq 내에서 x가 삽입되어야 할 가장 오른쪽 인덱스 반환
5. __collections__: from collections import Counter
> - counter = Counter(리스트 || 문자열): unique한 요소들의 개수를 파악할 수 있다.
>    * counter.most_common(n): 최빈값 n개 반환
>    * Counter끼리는 연산이 가능하다!
  

## 자바 기본
1. __객체 지향 언어__
>- __객체__(object)란 클래스의 인스턴스나 배열
>- __클래스__ 는 멤버 변수와 메서드를 가지는 객체를 만들기 위한 확장이 가능한 코드 양식
>    * 객체를 만들기 위한 설계도
>- __인스턴스__ 란 클래스에 따라 메모리상에 구현된 실체

2. 자바 프로그램
>- 자바 프로그램은 한 개 이상의 클래스로 구성된다.
>- 클래스는 한 개 이상 필드(field)나 메소드(method)로 구성된다.
 ```java
  class Test {
    int field1;
    String field2;

    public void method1() {
        System.out.println("자바 프로그래밍!!");
    }
}
```
3. 타입
>- __변수__:데이터를 저장할 수 있는 메모리 공간
>    * 정수형: byte(-128 ~ 127), short(-2^15 ~ (2^15 - 1)), int(-2^31 ~ (2^31 - 1)), long
>    * 실수형: float(소수 6자리), double(소수 14자리)
>    * 문자형: char
>    * 논리형: boolean
>- __상수__: 데이터를 저장할 수 있는 메모리 공간, 변경 불가!
>    * 선언과 동시에 반드시 초기화해야 한다!
>    * __final__ int AGES = 30;
>    * 자바에서 상수의 이름은 일반적으로 모두 대문자를 사용하여 선언
> __타입변환__
>    * 묵시적 타입 변환: 자바에서는 데이터의 손실이 발생하지 않거나, 최소화되는 방향으로 묵시적 타입 변환을 진행
>    * 명시적 타입 변환: (변환할타입) 변환할데이터
```java
int num1 = 1, num2 = 4;
① double result1 = num1 / num2;
② double result2 = (double) num1 / num2;

System.out.println(result1); // 0.0 
// 자바에서 산술 연산을 수행하고 얻는 결괏값의 타입은 언제나 피연산자의 타입과 일치해야 합니다.
// 따라서 1 나누기 4의 결과로는 0.25가 반환되지만, int형으로 자동 타입 변환되어 0이 반환되게 됩니다.
// 그리고서 double형 변수에 그 결과가 대입될 때, double형으로 자동 타입 변환되어 0.0이라는 결과가 출력되게 됩니다.
System.out.println(result2); // 0.25
```

4. 연산자
>- __증감 연산자__: 피연산자를 1씩 증가 혹은 감소
>    * ++x, --x : 먼저 피연산자의 값을 1 증가/감소시킨 후에 해당 연산을 진행함.
>    * x++, x-- : 먼저 해당 연산을 수행하고 나서, 피연산자의 값을 1 증가/감소시킴.
>- __삼항 연산자__: 조건식 ? 반환값1 : 반환값2

5. 배열
>- 1차원 배열
>    * 타입[] 배열이름 = new 타입[배열길이]; int[] grade1 = new int[3];
>    * 배열의 초기화
```java
int[] grade1 = {70, 90, 80};          // 배열의 선언과 동시에 초기화할 수 있음.
int[] grade2 = new int[]{70, 90, 80}; // 배열의 선언과 동시에 초기화할 수 있음.

int[] grade3;
// grade3 = {70, 90, 80};             // 이미 선언된 배열을 이 방법으로 초기화하면 오류가 발생함.

int[] grade4;
grade4 = new int[]{70, 90, 80};       // 이미 선언된 배열은 이 방법으로만 초기화할 수 있음.
```
>- 배열 정렬하기
>    * Array.sort(배열이름)
>    * Array.sort(배열이름, 시작 index, 끝 index)
>- 다차원 배열
>    * 2차원 배열: int[][] arr = new int[2][3];
>    * 가변 배열: 2차원 배열을 생성할 때, 열의 길이를 명시하지 않음으로써 행마다 다른 길이의 배열을 요소로 저장할 수 있다.
```java
// 2차원 배열
int[][] arr = {
    {10, 20, 30},
    {40, 50, 60}
};
// 가변 배열
int[][] arr = new int[3][];
arr[0] = new int[2];
arr[1] = new int[4];
arr[2] = new int[1];
```
>- Array와 List의 차이
|Array|List|
|---|---|
|정해진 공간이 있고, 인덱스가 존재|인덱스가 없고, 앞의 요소가 삭제되면 새로 추가되는 요소가 그 공간에 저장될 수 있음|
|객체 생성시 크기 할당 필수|크기 할당 필요 X|
|삽입/삭제: 느림|삽입/삭제: 빠름|
|데이터 조회: 빠름|데이터 조회: 느림|
|크기: length|크기: size|

6. Collection
>- 많은 수의 데이터를 그 사용 목적에 적합한 자료구조로 묶어 하나로 그룹화한 객체
>- 컬렉션의 종류: Set, List, Queue, Map, Stack
>    * HashSet, TreeSet / LinkedList, Vector, ArrayList / LinkedList, PriorityQueue / Hashtable, HashMap, TreeMap
>- 주요 메서드
>    * boolean add(E e) : 현재 컬렉션에 데이터 객체 e를 추가
>    * boolean addAll (Collection c) : 현재 컬렉션에 컬렉션 c의 모든 데이터를 추가
>    * boolean contains(Object o) : 현재 컬렉션에 객체 o의 포함 여부를 반환
>    * boolean containsAll(Collection c) : 현재 컬렉션에 컬렉션 c의 모든 데이터가 포함되어있는지 여부를 반환
>    * boolean remove(Object o) : 현재 컬렉션에서 객체 o를 삭제
>    * boolean removeAll(Collection c) : 현재 컬렉션에서 컬렉션 c와 일치하는 데이터를 삭제
>    * boolean retainAll(Collection<?> c) : 현재 컬렉션에서 컬렉션 c와 일치하는 데이터만 남기고 나머지는 삭제
>    * void clear( ) : 현재 컬렉션의 모든 데이터를 삭제
>    * int size( ) : 현재 컬렉션에 포함된 데이터 개수를 반환 
>    * boolean isEmpty( ) : 현재 컬렉션이 비어있는지 여부를 반환



7. ArrayList
>- ArrayList는 Array와 List의 장점을 합친 것으로, 컬렉션의 한 종류이다.
>    * index로 식별자를 쓰는 것이 가능하고, 리스트 특성 그대로 크기를 동적으로 사용할 수 있다.
>- 선언 및 초기화
```java
ArrayList<Integer> integers1 = new ArrayList<Integer>(); // 타입 지정
ArrayList<Integer> integers2 = new ArrayList<>(); // 타입 생략 가능
ArrayList<Integer> integers3 = new ArrayList<>(10); // 초기 용량(Capacity) 설정
ArrayList<Integer> integers4 = new ArrayList<>(integers1); // 다른 Collection값으로 초기화
ArrayList<Integer> integers5 = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5)); // Arrays.asList()
```
>- 주요 메서드
>    * list.set(0, 15); idx 값을 value로 수정
>    * list.remove(0); idx 값 또는 삭제할 값
>    * list.indexOf(0); // indexOf는 찾고자 하는 값의 위치를 return (값이 없으면 -1 return)


8. 스트림
>- __스트림__: 람다를 활용해 배열과 컬렉션을 함수형으로 간단하게 처리할 수 있는 기술
>- 스트림의 특징
>    * 원본 데이터 소스를 변경하지 않고, 읽기만 한다.
>    * 일회용으로, 한 번 사용하면 닫혀서 재사용이 불가능
>    * 작업을 내부 반복으로 처리한다: forEach()는 매개변수에 대입된 람다식을 데이터 소스의 모든 요소에 적용한다.
>- 스트림 만들기
>    * 배열 스트림: Arrays.stream()
>    * 컬렉션 스트림: .stream()
>- 중간 연산(가공하기)
>    * Filtering: 스트림 내 요소들을 하나씩 평가해서 걸러냄
>    * Mapping: 스트림 내 요소들을 하나씩 특정 값으로 변환하는 작업
>    * Sorting: 스트림 내 요소들을 정렬하는 작업
```java
List<String> list = Arrays.asList("a","b","c");

// Filtering
Stream<String> stream = list.stream().filter(list -> list.contains("a"));

// Mapping
Stream<String> stream = list.stream()
	.map(String::toUpperCase);
	//[A,B,C]
    
    .map(Integers::parseInt);
    // 문자열 -> 정수로 변환

// Sorting
Stream<String> stream = list.stream()
	.sorted() // [a,b,c] 오름차순 정렬
    .sorted(Comparator.reverseOrder()) // [c,b,a] (내림차순)
    
List<String> list = Arrays.asList("a","bb","ccc");
Stream<String> stream = list.stream()
	.sorted(Comparator.comparingInt(String::length)) // [ccc,bb,a] //문자열 길이 기준 정렬

// 기타 연산
Stream<String> stream = list.stream()
	.distinct() // 중복 제거
    .limit(max) // 최대 크기 제한
    .skip(n)    // 앞에서부터 n개 skip하기
    .peek(System.out::println) // 중간 작업결과 확인
```
>- 최종 연산 (결과 만들기)
>    * Calculating: 최소, 최대, 합, 평균 등의 연산 수행 
>    * Reduction: 스트림의 요소를 하나씩 줄여가며 누적연산 수행
>    * Collecting: 스트림의 요소를 원하는 자료형으로 변환
>    * Matching: 특정 조건을 만족하는 요소가 있는 체크; anyMatch, allMatch, noneMatch
>    * Iterating: forEach로 스트림을 돌며 실행되는 작업
>    * Finding: 스트림에서 하나의 요소를 반환
```java
// Calculating
IntStream stream = list.stream()
	.count()   //스트림 요소 개수 반환
    .sum()     //스트림 요소의 합 반환
    .min()     //스트림의 최소값 반환
    .max()     //스트림의 최대값 반환
    .average() //스트림의 평균값 반환

// Reduction
IntStream stream = IntStream.range(1,5);
	.reduce(10, (total,num)->total+num);
    //reduce(초기값, (누적 변수,요소)->수행문)
    // 10 + 1+2+3+4+5 = 25

// Matching
List<String> members = Arrays.asList("Lee", "Park", "Hwang");
boolean matchResult = members.stream()
						.anyMatch(members->members.contains("w")); //w를 포함하는 요소가 있는지, True
boolean matchResult = members.stream()
						.allMatch(members->members.length() >= 4); //모든 요소의 길이가 4 이상인지, False
boolean matchResult = members.stream()
						.noneMatch(members->members.endsWith("t")); //t로 끝나는 요소가 하나도 없는지, True

//Iterating
members.stream()
	.map(Person::getName)
    .forEach(System.out::println);

// Finding
Person person = members.stream()
					.findAny()   //먼저 찾은 요소 하나 반환, 병렬 스트림의 경우 첫번째 요소가 보장되지 않음
                    .findFirst() //첫번째 요소 반환
```
