# 이진 탐색
>정렬돼 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터 탐색

**logN** 의 시간복잡도를 갖는다.
* * *
* 파이썬 이진탐색 라이브러리: from bisect import 
  * bisect_left(a,x): 리스트 a의 정렬 순서 유지하며 x를 삽입할 가장 왼쪽 인덱스 반환
  * bisect_right(a,x): 리스트 a의 정렬 순서 유지하며 x를 삽입할 가장 오른쪽 인덱스 반환
* __parametric search__ 문제를 이진탐색으로 해결 가능
  * 최적화 문제(최소, 최대를 구하는 문제)를 결정문제로 바꾸어 해결하는 기법
  * 특정 조건을 만족하는 가장 알맞은 값을 이분 탐색으로 빠르게 찾음
  * __특히 큰 탐색 범위__ 를 보면 이진 탐색을 떠올리는 게 좋음

* 반복문 구현
  ```python
  def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1 
    return None
  ```