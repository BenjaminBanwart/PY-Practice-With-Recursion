# Write code for algorithm 1 below

def func(num):
    if num == 0:
        return
    else:
        print(num)
        func(num-1)
n = 8

func(n)