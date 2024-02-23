import sys

def main(lines):
    black_tiles = 0
    white_tiles = 0
    turn = 1                    # Odd number: Black, Even numver: White
    reversi = [['B',1],['W',1]]             
    for turns in lines[0]:
#____________Black's turn__________________#
        if turn%2 != 0:         
            if turns=='R':      # Insert to right
                if len(reversi)==1:
                    reversi.append(['B',1])
                elif reversi[0][0]=='B':        # Flip tiles
                    reversi[0][1]+=1
                    reversi[0][1]+=reversi[1][1]
                    reversi.pop(1)
                else:
                    reversi[1][1]+=1
                turn+=1
            else:               # Insert to left 
                if len(reversi)==1:
                    reversi.insert(0,['B',1])
                elif reversi[1][0]=='B':        # Flip tiles
                    reversi[1][1]+=1
                    reversi[1][1]+=reversi[0][1]
                    reversi.pop(0)
                else:
                    reversi[0][1]+=1                   
                turn+=1
 #___________ White's turn___________________#
        else:                  
            if turns=='R':      # Insert to right
                if len(reversi)==1:
                    reversi.append(['W',1])
                elif reversi[0][0]=='W':        # Flip tiles
                    reversi[0][1]+=1
                    reversi[0][1]+=reversi[1][1]
                    reversi.pop(1)
                else:
                    reversi[1][1]+=1
                turn+=1
            else:               # Insert to left 
                if len(reversi)==1:
                    reversi.insert(0,['W',1])
                elif reversi[1][0]=='W':        # Flip tiles
                    reversi[1][1]+=1
                    reversi[1][1]+=reversi[0][1]
                    reversi.pop(0)
                else:
                    reversi[0][1]+=1                   
                turn+=1
#__________Counting tiles______________#
    for final in reversi:
        if final[0]=='B':
            black_tiles = final[1]
        else:
            white_tiles = final[1]

    print(f'{black_tiles} {white_tiles}')

    

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
