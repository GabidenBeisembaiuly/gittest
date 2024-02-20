n = int(input())
gen = (i**2 for i in range(n))
for num in gen:
    print(num)