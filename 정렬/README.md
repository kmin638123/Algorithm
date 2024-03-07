# 정렬

|O($N^2$) 시간 복잡도|O($NlogN$) 시간 복잡도|
|---|---|
|버블 정렬|병합 정렬|
|선택 정렬|힙 정렬|
|삽입 정렬|부드러운 정렬|
|퀵 정렬|

|__스택__ or __재귀함수__ 이용|__큐__ 이용|

## 선택 정렬

>처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞 데이터와 바꾸는 것을 반복

**이중 반복문** (O($N^2$)) 사용 

* 소스코드
  ```python
  for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스

    # 처리되지 않은 데이터 중에서 가장 작은 데이터를 찾음
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    
    array[i], array[min_index] = array[min_index], array[i] # 스와프
  ```

* swap

  ```python
  array[i], array[min_index] = array[min_index], array[i]
  ```

## 삽입 정렬

>처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입함

**이중 반복문** (O($N^2$))이지만, 최선 O($N$) 가능

* 소스코드
  ```python
  for i in range(len(array)):
    for j in range(i, 0, -1): # 인덱스 i 부터 1씩 감소
        if array[j] < array[j-1] # 자기보다 왼쪽 데이터가 크면
            array[j], array[j-1] = array[j-1], array[j] # 왼쪽으로 이동
        else: # 자기보다 작은 데이터를 만나면 
            break # 그 위치에서 멈춤
  ```

* 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 최선 O($N$)의 시간 복잡도

## 퀵 정렬

> 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈

(O($NlogN$))이지만, 최악 O($N^2$) 가능

* 소스코드
  ```python
  def quick_sort(array):
    if len(array)<=1: # 원소가 1개인 경우 종료 
        return array

    pivot = array[0]
    tail = array[1:]
    
    left = x[x for x in tail if x<=pivot]
    right = x[x for x in tail if x>pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)
  ```

* 첫 번째 원소를 피벗으로 삼을 때, 이미 정렬된 배열에 대해 퀵 정렬을 수행하면 최악 O($N^2$)의 시간 복잡도

## 계수 정렬
> 앞 정렬들과 다르게 데이터 값을 직접 비교하지 않고, 단순하게 각 숫자가 몇 개 있는지를 개수를 세어 저장한 후에 정렬

값 비교가 일어나지 않기 때문에 매우 빠르게 동작하지만, 개수를 저장하는 배열이 사용되기 때문에 추가 공간이 필요하다. 또한, 데이터 크기 범위가 제한되어 정수형태로 편할 수 있을 때 사용 가능하다.

데이터 개수가 N, 데이터(양수) 중 최댓값이 K일 때, 최악의 경우에도 수행시간 O($N+K$) 보장

* 소스코드
  ```python
  count = [0] * (max(array) + 1)
  
  for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값을 증가시킴

  for i in range(len(count)): 
    for j in range(count[i]):
        print(i, end=" ")
  ```

* 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적으로 사용

## 병합 정렬

> 하나의 리스트를 두 개의 균등한 크기의 리스트로 분할하고, 분할된 부분 리스트를 정렬 한 다음, 두 개의 정렬된 부분 리스트를 합하여 전체가 정렬되도록 한다.

(O($NlogN$))이지만, 최악 O($N$) 가능

* 소스코드
  ```python
  def merge_sort(arr):
    if len(arr)<2:
      return arr
    
    mid = len(arr)//2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    return merge(low_arr, high_arr)

  def merge(left, right):
    merged_arr = []
    l = h = 0
    while l<len(left) and h < len(right):
      if left[l]< right[h]:
        merged_arr.append(left[l])
        l+=1
      else:
        merged_arr.append(right[h])
        h+=1
    
    # 한 쪽 리스트에만 남아 있는 경우
    merged_arr += left[l:]
    merged_arr += right[h:]

    return merged_arr 
  ```

* 두 개의 배열을 병합할 때, 병합 결과를 담아 놓을 배열이 추가로 필요하므로 공간 복잡도는 O(N)이다.
* 다른 정렬 알고리즘과 달리 swap이 일어나지 않는다.
* 병합 정렬은 세 가지 단계로 이루어진다. 
  1) __분할__: 같은 크기의 2개의 부분 배열로 분할한다.
  2) __정복__: 부분 배열을 정렬한다. 부분 배열의 크기가 크면 다시 순환 호출을 이용해 분할한다.
  3) __결합__: 정렬된 부분 배열을 하나로 합친다.


## 힙 정렬

> 최대 힙 트리(내림차순 정렬)나 최소 힙 트리(오름차순 정렬)를 구성해 정렬함

항상 (O($NlogN$)) 보장

* 힙 정렬은 다음과 같은 단계로 이루어진다.
  1) __heapify__! 정렬하고자 하는 배열을 힙으로 만든다.
  2) root를 마지막 노드와 교체
  3) 정렬될 때까지 1~2번 과정을 반복한다.

* 소스코드 (최대 힙 트리)
  ```python
  def max_heapify(arr, index, heap_size): 
    # arr: 힙으로 만들고자 하는 배열
    # index: 선택된 노드
    # heap_size: 힙의 범위

    largest = index # 부모 노드의 인덱스로 초기화
    left = 2 * index +1 # 왼쪽 자식 노드의 인덱스
    right = 2 * index +2 # 오른쪽 자식 노드의 인덱스

    # 선택노드, 선택 노드의 양 자식 중 가장 작은 값을 찾는 과정
    if left < heap_size and arr[right] > arr[largest]:
      largest = left 
    if right < heap_size and arr[right] > arr[largest]:
      largest = right
      
    # 선택 노드와 자식 노드의 위치가 바뀌어야 하면
    if largest != index:
      # 부모 자식 위치 변경
      arr[largest], arr[index] = arr[index], arr[largest]
      # 계속 바뀌어야 하는지 재귀적으로 체크
      heapify(arr, largest, heap_size)

  def heap_sort(unsorted):
    n = len(unsorted)

    # max heap 만드는 과정!!
    for i in range(n // 2 - 1, -1, -1):
      heapify(unsorted, i, n)
    
    # 루트노드와 마지막 노드를 교체하고 heapify 반복
    for i in range(n - 1, 0, -1):
      unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
      heapify(unsorted, 0, i)
    
    return unsorted
  ```
