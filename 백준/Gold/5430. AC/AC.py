from curses import qiflush
import sys
from collections import deque

N = int(sys.stdin.readline())

for i in range(N) :
    # 수행할 함수
    func = sys.stdin.readline().rstrip()
    
    # 배열의 원소 개수
    count = int(sys.stdin.readline())

    # 문자열에서 '['  ,  ']' 를 제거하고 , 기준으로 분리한 뒤 큐에 담기
    q = deque(sys.stdin.readline().rstrip()[1:-1].split(','))

    # 빈 배열이어도 R이 수행할 수 있어야하니, queue를 초기화
    if count == 0 :
        q = []
    
    r_count = 0
    flag = 0

    for i in func : 
        if i == 'R' :
            r_count += 1
        else :
            if len(q) == 0 :
                print('error')
                flag = 1
                break
            else :
                if r_count % 2 == 0 :
                    q.popleft()
                else :
                    q.pop()

    if flag == 1:
        continue
    else :
        if r_count % 2 == 0 :
            print('[' + ",".join(q) + ']')
        else :
            q.reverse()
            print('[' + ",".join(q) + ']')