def solution(boards, k):
    answer = 0
    for idx, board in enumerate(boards):
        for i, j in enumerate(board):
            if idx + i <= k:
                answer += j
    return answer
