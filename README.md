# Algorithm Study

## 라이브러리
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
