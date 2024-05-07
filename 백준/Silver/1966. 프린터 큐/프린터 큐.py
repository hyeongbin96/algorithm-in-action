import sys
from collections import deque

# 테스트 케이스
T = int(sys.stdin.readline())

for _ in range(T) :
    # 문서 수(N), 문서 위치(M), 문서의 우선순위 큐
    N, M = map(int, sys.stdin.readline().split())
    prio = deque(map(int, sys.stdin.readline().split()))
    # 문서 큐
    doc = deque(i for i in range(N))
    count = 0

    while True :
        if prio[0] == max(prio) :   # 우선순위 큐의 첫번째 인덱스가 가장 높은 경우
            count += 1
            if doc[0] == M :    # 궁금한 문서(M)가 문서의 첫번째 순서인 경우
                print(count)
                break
            else :
                del prio[0]
                del doc[0]
        else :
            prio.append(prio.popleft())
            doc.append(doc.popleft())