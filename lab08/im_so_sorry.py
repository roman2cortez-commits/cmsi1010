def blocks(n):
    if n <= 0:
        return 0
    else:
        return blocks(n - 1) + n

print(blocks(8))
print(blocks(0))
print(blocks(-1))
print(blocks(1))
print(blocks(838))

def sum_of_didgets(n):
    if n <= 10:
        return n
    else:
        return sum_of_didgets(n // 10) + (n % 10)

    return