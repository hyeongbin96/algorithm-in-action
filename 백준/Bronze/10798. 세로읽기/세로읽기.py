# ['ABCDE', 'abcde', '01234', 'FGHIJ', 'fghij']
# [['ABCDE'], ['abcde'], ['01234'], ['FGHIJ'], ['fghij']]
# 위 2개의 리스트에서 LIST[0][1] 시 아래 리스트는 안되는 이유 파악하기

board = []      # board = ["AABCDD", "afzz", "09121", "a8EWg6", "P5h3kx"]  
word_len = []   # word_len = [6, 4, 5, 6, 6]

for i in range(5) :
    word = input()
    board.append(word)
    word_len.append(len(word))

for i in range(max(word_len)) :     # 각 행의 첫 문자열을 순차적으로 입력할 때, 각 행의 길이보다 문자열이 작은 경우 입력
    for j in range(5) :             # ex) 1행을 기준으로 [0][0], [0][1] ... < len(1행)
        if i < word_len[j] :        # i = 각 행의 문자열 길이 ex) i=3일 때, 행의 4열 값임
            print(board[j][i], end='')