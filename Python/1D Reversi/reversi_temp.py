import sys

def main(lines):
    turn = 1                    # Odd number: Black, Even numver: White
    reversi = [1,0]             # 1:black, 0:white
    for turns in lines[0]:
        if turn%2 != 0:         # Black's turn
            if turns=='R':      # Insert to right
                reversi.append(1)
                # Traverse through list to see if any tiles need to be flipped
                for i in range(len(reversi)-2,-1,-1):
                    if reversi[i]==1:
                        for tile in range(i+1,len(reversi)-1):
                            reversi[tile] = 1
                        break
                turn+=1
            else:               # Insert to left                    
                reversi.insert(0,1)
                # Traverse through list to see if any tiles need to be flipped
                for i in range(1,len(reversi)):
                    if reversi[i]==1:
                        for tile in range(1,i):
                            reversi[tile] = 1
                        break
                turn+=1
        else:                   # White's turn
            if turns=='R':      # Insert to right
                reversi.append(0)
                # Traverse through list to see if any tiles need to be flipped
                for i in range(len(reversi)-2,-1,-1):
                    if reversi[i]==0:
                        for tile in range(i+1,len(reversi)-1):
                            reversi[tile] = 0
                        break
                turn+=1
            else:               # Insert to left                    
                reversi.insert(0,0)
                # Traverse through list to see if any tiles need to be flipped
                for i in range(1,len(reversi)):
                    if reversi[i]==0:
                        for tile in range(1,i):
                            reversi[tile] = 0
                        break
                turn+=1

    print(f'{reversi.count(1)} {reversi.count(0)}')

    

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
