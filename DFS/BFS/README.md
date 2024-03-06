# DFS/BFS
> 그래프 탐색 알고리즘

<details>
<summary>그래프란?</summary>
<div markdown="1">       
- node와 그 node를 연결하는 edge로 이루어진 자료구조  

-__트리__ 도 방향성이 있는 비순환 그래프이며, 부모-자식 관계가 있는 계층 모델

</div>
</details>

* * *
|DFS|BFS|
|---|---|
|깊이 우선 탐색|너비 우선 탐색|
|현재 노드에서 갈 수 있는 모든 노드 탐색|가까운 노드부터 우선적으로 탐색|
|한 경로를 우선적으로 깊게 탐색하기 때문에 <br> 경로의 특징을 저장해야 하는 문제에 유용|현재 노드에서 가까운 곳부터 찾기 때문에 <br> 최단거리 구해야 하는 문제에 유용|
|__스택__ or __재귀함수__ 이용|__큐__ 이용|

|스택 (DFS)|큐 (BFS)|
|---|---|
|LIFO (후입선출)|FIFO (선입선출)|
|리스트 이용 <br> stack = []|from collections import deque <br> queue = deque()|
|stack.append(x)|queue.append(x)|
|stack.pop()|queue.popleft()|



## DFS 구현

DFS는 스택으로 간단히 구현할 수 있지만, 재귀함수를 이용하여 매우 간결히 구현할 수 있다!

```python
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end="") # 방문한 노드 출력

    for i in graph[v]:
        if not visited[v]:
            dfs(graph, i, visited)

dfs(graph,1,visited)
```   

### 백트래킹
__특정 조건을 만족하는 경우__ 에만  __DFS 탐색__ 을 진행하는 알고리즘
> 해를 찾는 도중에 어떤 노드가 유망하지 않다고 판단되면 더 이상 깊게 들어가지 않고, 그 노드의 이전으로 되돌아가서 해를 찾음


* 대표 유형 문제: [N-Queen](https://www.acmicpc.net/problem/9663)
  * 유망한 노드: 가로, 세로, 대각선에 퀸이 없는 좌표 

## BFS 구현

bfs의 결과는 __항상 최단 경로__!!

```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end="")

        for i in graph[v]:
            if not visited[v]:
                queue.append(i)
                visited[i]=True

bfs(graph,  1, visited)
```   