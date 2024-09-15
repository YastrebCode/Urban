def get_matrix(n, m, value):
    if n <= 0 or m <= 0 or value <= 0:
        return []
    tmp = []
    for i in range(0, m):
        tmp.append(value)
    m = []
    for i in range(0, n):
        m.append(tmp)
    return m

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)