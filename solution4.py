# Write code for algorithm 4 below


def func(base, exponent):
    if exponent==0:
        return 1
    else:
        return base*func(base,exponent-1)

a=3
b=5
print(func(a,b))