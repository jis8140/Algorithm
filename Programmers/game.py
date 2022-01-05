def solution(board, moves):
    answer = 0
    arr = []
    stack = []

    for i in range(len(board[0])):
        line = []
        for j in range(len(board)):
            if board[j][i] != 0:
                line.append(board[j][i])
        arr.append(line)

    for i in moves:
        if len(arr[i-1]) != 0 and len(stack) != 0:
            temp = arr[i-1].pop(0)
            if temp == stack[-1]:
                stack.pop()
                answer += 2
            else:
                stack.append(temp)
        elif len(arr[i-1]) != 0:
            temp = arr[i-1].pop(0)
            stack.append(temp)

    return answer