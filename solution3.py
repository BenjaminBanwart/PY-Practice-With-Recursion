# Write code for algorithm 3 below

def func(n):
    if n <= 1:
        return n
    else:
        print(n)
        return(func(n-1)+func(n-2))

n=2
for i in range(n):
    print(func(i))