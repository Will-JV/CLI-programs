import sys

def main(lines):
    board = lines[0]
    maximum = 0
    temp = 0
    empty = []
    for i in range(len(board)):
        if board[i]=='.':
            empty.append(i)
    
    for space in empty:
        # Check for white to left
        if 'W' in board[0:space] or board[space+1:]:
            temp = 0
            temp2 = 0
            if 'W' in board[0:space]:
                for i in range(space-1,0,-1):
                    if board[i] == 'B':
                        temp += 1
                    elif board[i] == '.':
                        temp = 0
                        break
                    else:
                        break
         # Check for white to right
            if 'W' in board[space+1:]:
                for i in range(space+1,len(board)):
                    if board[i] == 'B':
                        temp2 += 1
                    elif board[i] == '.':
                        temp2 = 0
                        break
                    else:
                        break
            if (temp+temp2)>maximum:
                maximum = temp+temp2

        # Check for black to left
        if 'B' in board[0:space] or board[space+1:]:
            temp = 0
            temp2=0
            if 'B' in board[0:space]:
                for i in range(space-1,0,-1):
                    if board[i] == 'W':
                        temp += 1
                    elif board[i] == '.':
                        temp = 0
                        break
                    else:
                        break
         # Check for black to right
            if 'B' in board[space+1:]:
                for i in range(space+1,len(board)):
                    if board[i] == 'W':
                        temp2 += 1
                    elif board[i] == '.':
                        temp2 = 0
                        break
                    else:
                        break
            if (temp+temp2)>maximum:
                maximum = temp+temp2
    # Print answer
    print(str(maximum))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

