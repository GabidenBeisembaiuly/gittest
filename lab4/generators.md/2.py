def func(n):
    for i in range(n):
        if (i % 2 == 0):
            yield i
    


n = int(input())
mylist = list(func(n))
print (mylist)