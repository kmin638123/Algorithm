# 그리디 알고리즘
>현재 상황에서 지금 당장 좋은 것만 고르는 방법!

**단순히 가장 좋은 것만 반복적으로 선택해도 최적의 해를 보장하는 검토해야 한다!**

* * *
어떤 문제들이 그리디 유형에 속할까?
* 거스름 돈 문제
  * [이코테 영상](https://www.youtube.com/watch?v=2zjoKjt97vQ)
  * N원을 500원/100원/50원/10원 만으로 거슬러 주어야 할 때, 필요한 동전의 최소 개수 구하기
  * __큰 단위가 항상 작은 단위의 배수인 경우__, 가장 큰 화폐의 단위부터 돈을 거슬러 주는 것이 최적의 해를 보장한다!
* N이 1이 될 때까지
  * [이코테 영상](https://www.youtube.com/watch?v=2zjoKjt97vQ)
  * N이 1이 될 때까지, N에서 1을 빼거나 N을 K로 나누는 연산을 반복한다. 이때, 나누는 연산은 N이 K로 나누어떨어질 때만 가능하다.
  * 연산 최소 횟수를 구하는 문제로, 나누는 연산이 N의 값을 1로 빠르게 가까워지게 하므로, N을 최대한 많이 나누면 된다! 

   ```python
    While True:
        target = (N//K) * K # K로 나눠 떨어지는 N과 가까운 수 찾기
        result += (N-target) # 1을 빼야 하는 횟수
        N = target
        if N < K: # 더이상 N을 K로 나눌 수 없는 경우!
            break
        result += 1
        N //= K
    result += (N-1)
    ```
* 조이스틱
  * [프로그래머스 문제](https://programmers.co.kr/learn/courses/30/lessons/42860)
  * 좌우 이동 횟수 구하는 것이 관건이다! 처음에는 모두 A로 이루어져 있으므로 A는 상하로 이동할 필요가 없다.
  * 따라서 A가 연속되어 있는 구간은 들리지 않도록 해서 좌우 이동 횟수를 최소화할 수 있도록 한다.
  ```python
    def solution(name):
        answer = 0
        turn = len(name)-1 # 가능한 최대 좌우 이동 횟수

        for i in range(0, len(name)):

            # 상하 이동 횟수 구하기
            up = ord(name[i]-ord("A"))
            down = 1+ord("Z")-ord(name[i])
            plus = up if up < down else down
            answer += plus

            # 각 문자마다 최소 좌우 이동 횟수 구하기
            ind = i+1 # i 다음에 있는 A가 아닌 문자
            while ind < len(name) and name[ind] == "A":
                ind += 1
            turn = min(turn, i+len(name)-ind+min(i, len(name)- ind))

        return answer + turn
    ```
  * turn 구하는 코드: i+len(name)-ind+min(i, len(name)- ind)  
  좌우 중에 더 최단 거리(min)인 방향을 선택하면 된다.
    * 좌: 원점 -> ind -> 원점 -> i
    * 우: 원점 -> i -> 원점 -> ind

* 큰 수 만들기
  * [프로그래머스 문제](https://school.programmers.co.kr/learn/courses/30/lessons/42883)
  * input "number" 앞에 있는 숫자부터 스택에 넣어서, push될 값(n)보다 작은 값들이 stack에 있으면 pop()!
  * pop()이 수행되는 횟수만큼이 수를 제거하는 횟수가 된다!
  ```python
    def solution(number, k):
        stack = []
        for n in number:
            while stack and stack[-1] < n and k > 0:
                stack.pop()
                k -= 1
            stack.append(n)
        
        # 아직 제거되지 못한 숫자를 뒤에서부터 삭제
        if k > 0:
            stack = stack[:-k]

        return ''.join(stack)
    ```

* 섬 연결하기
  * [프로그래머스 문제](https://school.programmers.co.kr/learn/courses/30/lessons/42861)
  * __kruskal 알고리즘__ 을 이용해 최적의 해를 찾는다!  
    <details>
    <summary>kruskal 알고리즘이란?</summary>
    <div markdown="1">       
    - 네트워크의 모든 정점을 최소 비용으로 연결하는 최적 해답을 구하는 것.  

    -각 단계에서 __사이클을 이루지 않는__ 최소 비용 간선을 선택한다. 
    
    >    1. 그래프 간선들을 가중치의 오름차순으로 정렬  
    >    2. 정렬된 간선 그래프에서 순서대로 사이클을 형성하지 않는 간선 선택
    >   * [__union-find 알고리즘__](https://github.com/kmin638123/Algorithm/blob/master/%EC%84%9C%EB%A1%9C%EC%86%8C%20%EC%A7%91%ED%95%A9/README.md#%EC%84%9C%EB%A1%9C%EC%86%8C-%EC%A7%91%ED%95%A9) 사용!
    >   3. 해당 간선을 현재의 MST의 집합에 추가.
    >   * MST: 스패닝 트리 중에서 사용된 간선들의 가중치 합이 최소인 트리
    
    <span style="color:gray">(출처: [[알고리즘] Kruskal 알고리즘 이란](https://gmlwjd9405.github.io/2018/08/29/algorithm-kruskal-mst.html))</span>
    

    </div>
    </details>
  ```python
    def solution(n, costs):
        
        costs.sort(key = lambda x:x[2]) # cost 기준으로 오름차순 정렬
        lilnk = set() # MST 집합 생성
        link.add(costs([0][0]))
        answer = 0

        while len(link)!=n:
            for v in costs:
                if v[0] in link and v[1] in link:
                    continue # 바로 다음 순번의 loop 수행
                if v[0] in link or v[1] in link:
                    link.update([v[0], v[1]])
                    answer+=v[2]
                    break # for문 밖으로 나감!

        return answer
    ```   

    