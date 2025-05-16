cube = lambda x: x**3

def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

# Sample Input:
# 5

# Sample Output:
# [0, 1, 1, 8, 27]