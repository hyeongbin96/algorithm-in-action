def solution(rsp):
    answer = ""
    game = {
        "2": "0",
        "0": "5",
        "5": "2",
    }
    return ''.join(game[i] for i in rsp)