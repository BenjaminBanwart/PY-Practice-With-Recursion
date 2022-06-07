# Write code for algorithm 5 below

def func(string):
    if string != string[::-1]:
        return False
    else:
        return True

func('racecar')