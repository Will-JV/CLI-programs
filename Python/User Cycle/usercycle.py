import sys

def main(lines):
    n = int(lines[0].split()[0])
    m = int(lines[0].split()[1])
    a = {}
    x = 1
    user_cycle = 0
    for ele in lines[1:]:
        temp = ele.split()
        if int(temp[0]) in a:
            a[int(temp[0])].append(int(temp[1]))
        else:
            a[int(temp[0])] = [int(temp[1])]
    for first in range(1,n+1):
        for second in range(first+1,n+1):
            for third in range(second+1,n+1):
                no = 0
                try:
                    test = a[first]
                    test = a[second]
                    test = a[third]
                except KeyError:
                    no = 1
                if no == 0:
                    if second in a[first]:
                        if third in a[second]:
                            if first in a[third]:
                                user_cycle += 1
                                no = 1
                if no == 0:
                    if third in a[first]:
                        if second in a[third]:
                            if first in a[second]:
                                user_cycle += 1
    print(str(user_cycle))




if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
