import multiprocessing as m
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    start=time.time()
    a = m.Process(target=counter, args = (83333333,))
    b = m.Process(target=counter, args = (83333333,))
    c = m.Process(target=counter, args = (83333333,))
    d = m.Process(target=counter, args = (83333333,))
    e = m.Process(target=counter, args = (83333333,))
    f = m.Process(target=counter, args = (83333333,))
    g = m.Process(target=counter, args = (83333333,))
    h = m.Process(target=counter, args = (83333333,))
    i = m.Process(target=counter, args = (83333333,))
    j = m.Process(target=counter, args = (83333333,))
    k = m.Process(target=counter, args = (83333333,))
    l = m.Process(target=counter, args = (83333337,))
    
    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()
    i.start()
    j.start()
    k.start()
    l.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()
    i.join()
    j.join()
    k.join()
    l.join()
    
    print(a)
    print(f'time = {time.time()-start}','s')


if __name__ == '__main__':
    main()
