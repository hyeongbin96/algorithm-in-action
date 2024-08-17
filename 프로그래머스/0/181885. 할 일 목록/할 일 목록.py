def solution(todo_list, finished):
    return [todo_list[idx] for idx, value in enumerate(finished) if value == False]