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