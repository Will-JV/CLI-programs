def solution(A):
    A.sort()
    a = {}
    for num in A:                               #creating keys for each integer that exists
        if num not in a:
            a[num] = 1
    for i in range(1,A[-1]):                    #searching for smallest non-existent integer if list is more than 0
        try:
            result = a[i]
        except KeyError:
            return i
    if A[-1]<=0:                                #if largest integer is negative return 1
        return 1
    else:                                       
        result = A[-1]+1
        return result

    
    
A = [1,3,6,4,1,2]
solution(A)


