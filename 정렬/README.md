# 정렬

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
