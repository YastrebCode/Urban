numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = numbers
del numbers
not_Primes = []
for i in primes:
    for a in range(1, i + 1):
        if a != 1 and a != i and i % a == 0:
            not_Primes.append(i)
            break
for i in not_Primes:
    primes.remove(i)
try:
    primes.remove(1)
except Exception as e:
    pass
print(f'Primes: {primes}\nNot Primes: {not_Primes}')