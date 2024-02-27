# Algorithm Study

## 라이브러리
1. __sys__: import sys
- sys.stdin.readline()
- sys.setrecursionlimit(10 ** 6)
  * 재귀 사용 문제에서 필수!
  * 파이썬 기본 재귀 깊이 제한 = 1000
2. __itertools__: from itertools  import ~
- list(permutations(data, a)): 순열 (a개 뽑아 나열)
- list(combinations(data, b)): 조합 (b개 뽑아 순서없이 나열)
- list(product(data, repeat=c)): 중복 순열 (총 c개 뽑아 나열)
- list(combinations_with_replacement(data, d)): 중복 조합
3. __heapq__: import heapq
- heapq.heappush(h, value) || heapq.heappush(h, -value)
- heapq.heappop(h) || -heapq.heappop(h)
4. __bisect__: from bisect import ~
- bisect.bisect_left(seq, x, lo=0, hi=None): 정렬된 seq 내에서 x가 삽입되어야 할 가장 왼쪽 인덱스 반환
  * lo, hi는 탐색 범위를 지정하는 인덱스, 보통은 생략
- bisect.bisect_right(seq, x, lo=0, hi=None): 정렬된 seq 내에서 x가 삽입되어야 할 가장 오른쪽 인덱스 반환
5. __collections__: from collections import Counter
- counter = Counter(리스트 || 문자열): unique한 요소들의 개수를 파악할 수 있다.
  * counter.most_common(n): 최빈값 n개 반환
  * Counter끼리는 연산이 가능하다!
  