# Write code for algorithm 2 below

def func(ln, num):
    if ln > num:
        return
    else:
        print(ln)
        func(ln + 1, num)

n = 5
func(1, n)