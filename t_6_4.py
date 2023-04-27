def find_duration(x, y, percent=10):
    p = 0.01 * percent
    res = x
    it = 1
    while res < y:
        res = res * (1 + p) 
        it += 1
    return it


x = float(input())
y = float(input())

print(find_duration(x, y, percent=10))
