# 동적 계획법
>하나의 큰 문제를 여러 개의 작은 문제로 나누어서 그 결과를 저장 (__메모이제이션__)하여 다시 큰 문제를 해결할 때 사용

재귀적 호출에서 중복 계산을 방지하고 계산 속도를 향상 시킨다.

## DP 기법을 사용할 수 있는 조건
1. __최적 부분 구조__: 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아 큰 문제를 해결할 수 있어야 한다.
2. __중복되는 부분 문제__: 동일한 작은 문제를 반복적으로 해결할 수 있어야 한다.

## DP 구현 방식
1. __top down__ (하향식): 메모이제이션
- 큰 문제를 작은 부분 문제로 나누어 해결하는 방식
- caching: 한 번 계산된 작은 문제의 결과를 메모리 공간에 메모한다.
- 같은 문제를 다시 호출하면, 메모했던 결과를 메모리 공간에서 그대로 가져온다.
- 대표적인 문제: __피보나치 수열__
2. __bottom up__ (상향식): DP 테이블
- 작은 부분 문제부터 차례대로 해결해 큰 문제를 해결하는 방식
- 재귀: 반복문을 사용하여 부분 문제를 해결하고, 결과를 DP 테이블(배열) 등에 저장한다.
- [a,b] = [a-1,b] + [a,b-1]

## DP 유형 문제
* 개미전사
  * [이코테 영상](https://www.youtube.com/watch?v=5Lu34WIx2Us)
  * 근접한 창고는 털 수 없을 때, 얻을 수 있는 식량의 최댓값을 구하는 문제
  * 점화식: $a_n = max(a_{n-1}, a_{n-2}+k_n)$
  * __bottom up__ 방식

  ```python
  d = [0] * 100 # DP 테이블 초기화

  d[0] = array[0]
  d[1] = max(array[0], array[1])

  for i in range(2,n):
      d[i] = max(d[i-1], d[i-2]+array[i])  

  print(d[n-1])
  ```
* 효율적인 화폐 구성
  * [이코테 영상](https://www.youtube.com/watch?v=5Lu34WIx2Us)
  * n개의 화폐로 m원을 만들 때, 필요한 화폐의 최소 개수
  * 점화식: 각 화폐 단위인 k를 하나씩 확인하며
    * $a_{i-k}$를 만드는 방법이 존재하는 경우, $a_i=min(a_i, a_{i-k}+1)$
    * $a_{i-k}$를 만드는 방법이 존재하지 않는 경우, $a_i=INF$
  * __bottom up__ 방식

  ```python
  d = [10001] * (m+1) # DP 테이블 초기화

  d[0] = 0
  for i in range(n): # 각 화폐 단위를 하나씩 확인
      for j in range(array[i], m+1):
          if d[j-array[i]]!= 10001: # (i-k)원을 만드는 방법이 존재하는 경우
              d[j] = min(d[j], d[j-array[i]]+1)
              
  if d[m] == 10001: print(-1)
  else: print(d[m])
  ```

* 병사 배치하기
  * [이코테 영상](https://www.youtube.com/watch?v=5Lu34WIx2Us)
  * 제외하는 병사의 수를 최소로, 병사들의 전투력이 내림차순이 돼야 한다.
  * __가장 긴 증가하는 부분 수열__(LIS) 알고리즘 이용해서 가장 긴 감소하는 부분 수열을 찾는 문제
    * LIS 점화식:  D[i]가 array[i]를 마지막 원소로 갖는 부분 수열의 최대 길이일 때,   
    모든 $j\leq i$에 대해, $D[i] = max(D[i], D[j]+1)$ if $array[j]<array[i]$
  * __bottom up__ 방식

  ```python
  # array가 병사들의 전투력일 때
  array.reverse()

  d = [1] * (n) # DP 테이블 초기화
  
  for i in range(1,n):
      for j in range(0,i):
          if array[j] < array[i]:
              d[i] = max(d[i],d[j]+1)
  
  print(n-max(dp)) # 열외해야 하는 병사의 최소 수 출력
  ```
