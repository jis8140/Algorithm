import re

def solution(new_id: str) -> str:

    # Level_1
    new_id = new_id.lower()

    #   st = re.sub('[^a-z0-9\-_.]', '', st)
    # Level_2
    char_lower = [chr(c) for c in range(ord('a'), ord('z')+1)]
    integer = [chr(i) for i in range(ord('0'), ord('9')+1)]
    char_others = ['-', '_', '.']
    characters = char_lower + integer + char_others
    new_id = ''.join(char for char in new_id if char in characters)

    #   st = re.sub('\.+', '.', st)
    # Level_3
    answer = re.sub('((["."])\\2{1,})', '.', new_id)

    #   st = re.sub('^[.]|[.]$', '', st)
    # Level_4
    if len(answer) > 2:
        if answer[0] == '.':
            answer = answer[1:]
        if answer[-1] == '.':
            answer = answer[:-1]
    elif len(answer) == 2:
        if answer[0] == '.':
            answer = answer[1:]
        if answer[-1] == '.':
            if len(answer) == 1:
                answer = ''
            else:
                answer = answer[:-1]
    elif len(answer) == 1:
        if answer[0] == '.':
            answer = ''
        elif answer[-1] == '.':
            answer = ''

    #   st = 'a' if len(st) == 0 else st[:15]
    #   st = re.sub('^[.]|[.]$', '', st)
    # Level_5
    if len(answer) == 0:
        answer = 'a'

    # Level_6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    #   st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    # Level_7
    if len(answer) < 3:
        last = answer[-1]
        while len(answer) != 3:
            answer += last

    return answer