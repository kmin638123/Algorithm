# 서로소 집합
>무방향 그래프에서 사이클을 판별할 수 있는 방법!

**union-find 알고리즘을 사용한다.**

* * *
union-find 알고리즘은 무엇일까?
* __disjoint-set__(중복되지 않는 부분 집합들)을 표현할 때, 사용하는 알고리즘!
  * <span style="color:lightblue">__초기화__</span>: 노드의 개수가 v일 때,
    ```python
    parent = [0] * (v+1) # 부모 테이블 초기화

    for i in range(1, v+1):
        parent[i] = i # 부모를 자기 자신으로 초기화
    ```
  * <span style="color:lightblue">__union(x,y)__</span>: x, y가 속한 두 집합을 합치는 연산
    ```python
    def union(x, y):
        x = find(x)
        y = find(y)
        if x != y:
            parent[x]=y
    ```
  * <span style="color:lightblue">__find(x)__</span>: x가 속한 집합의 루트 노드 값 반환!  
    
    루트 노드는 부모 노드 번호 값이 자기 자신!
    ```python
    def find(x):
        # 루트 노드를 찾을 때까지 재귀 호출
        if parent[x]!=x:
            parent[x] = find(parent[x])
        return parent[x]
    ```