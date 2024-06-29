lst = [1,2,3,4,5,6,7,8,9,8,7,6,5,6]
lst_iter = iter(lst)

if lst[0] > lst[1]:
    print("pankaj")
for i, e in enumerate(lst[1:]):
    print(i, e)
    print(next(lst_iter))
    nxt=next(lst_iter)

    if i<=nxt:
        continue
    elif i==max(lst):
            print(i)

def check_call_correction(lst):
    lst.reverse()
    lst_iter = iter(lst)
    count=0
    for i, e in enumerate(lst[1:]):
        nxt=next(lst_iter)
        if i<nxt:
            count=count+1
        elif i==next:
            continue
        if count>3:
            return True

def check_put_correction(lst):
    lst.reverse()
    lst_iter = iter(lst)
    count=0
    for i, e in enumerate(lst[1:]):
        nxt=next(lst_iter)
        if i>nxt:
            count=count+1
        elif i==next:
            continue
        if count>3:
            return True

