import sys

def main(lines):
    if lines[0] == '1':
        total_food = int(lines[1])
        lines.pop(0)
        lines.pop(0)
        menu = {}
        table = {}
        counter=0
        while counter<total_food:
            food = lines[0].split()
            menu[food[0]] = [int(food[1]),int(food[2])]         #0=number,1=price
            lines.pop(0)
            counter += 1
        for orders in lines:
            order = orders.split()
            if menu[order[2]][0]>=int(order[3]):
                menu[order[2]][0] -= int(order[3])
                try:
                    table[order[1]][order[2]] += int(order[3])
                except KeyError:
                    temp = {order[2]:int(order[3])}
                    table[order[1]] = temp
                for i in range(int(order[3])):
                    print(f'received order {int(order[1])} {int(order[2])}')
            else:
                print(f'sold out {int(order[1])}')

    elif lines[0] == '2':
        total_microwave = int(lines[1].split()[1])
        microwave = int(lines[1].split()[1])
        total_food = int(lines[1].split()[0])
        lines.pop(0)
        lines.pop(0)
        menu = {}
        queue = []
        cooking = []
        counter=0
        while counter<total_food:
            food = lines[0].split()
            menu[food[0]] = [int(food[1]),int(food[2])]         #0=number,1=price
            lines.pop(0)
            counter += 1
        for instructions in lines:
            instruction = instructions.split()
            if instruction[0] == 'received':
                if microwave>0:
                    microwave -= 1
                    cooking.append(instruction[3])
                    print(instruction[3])
                else:
                    queue.append(instruction[3])
                    print('wait')
            elif instruction[0] == 'complete':
                if instruction[1] in cooking:
                    cooking.remove(instruction[1])
                    if len(queue)>0:
                        print('ok '+ queue[0])
                        cooking.append(queue[0])
                        queue.pop(0)
                    else:
                        microwave += 1
                        print('ok')    
                else:
                    print('unexpected input')
            else:
                print('unexpected input')

    elif lines[0] == '3':
        total_food = int(lines[1])
        lines.pop(0)
        lines.pop(0)
        menu = {}
        order = {}
        counter=0
        while counter<total_food:
            food = lines[0].split()
            menu[food[0]] = [int(food[1]),int(food[2])]         #0=number,1=price
            lines.pop(0)
            counter += 1
        for instructions in lines:
            instruction = instructions.split()
            if instruction[0] == 'received':
                try:
                    order[instruction[3]].append(instruction[2])
                except KeyError:
                    order[instruction[3]] = [instruction[2]]
            elif instruction[0] == 'complete':
                print('ready ' + order[instruction[1]][0] + ' '+ instruction[1])
                order[instruction[1]].pop(0)

    elif lines[0] == '4':
        total_food = int(lines[1])
        lines.pop(0)
        lines.pop(0)
        menu = {}
        order = {}
        price = {}
        counter=0
        while counter<total_food:
            food = lines[0].split()
            menu[food[0]] = [int(food[1]),int(food[2])]         #0=number,1=price
            lines.pop(0)
            counter += 1
        for instructions in lines:
            instruction = instructions.split()
            if instruction[0] == 'received':
                try:
                    order[instruction[2]].append(instruction[3])
                    price[instruction[2]] += menu[instruction[3]][1]
                except KeyError:
                    order[instruction[2]] = [instruction[3]]
                    price[instruction[2]] = menu[instruction[3]][1]
            elif instruction[0] == 'ready':
                order[instruction[1]].remove(instruction[2])
            elif instruction[0] == 'check':
                if instruction[1] in order:
                    if len(order[instruction[1]]) == 0:
                        print(str(price[instruction[1]]))
                        price[instruction[1]] = 0
                    else:
                        print('please wait')
                else:
                    print('0')

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
