from itertools import combinations;
resultLst = [];

def answer(l):
    l.sort(reverse = True);
    max_num = 0;
    for i in reversed(range(1, len(l)+1)):
        for tup in list(combinations(l, i)):
            print (tup);
            if sum(tup) % 3 == 0:
                return int(''.join(map(str, tup)));
            
    return 0;
                
