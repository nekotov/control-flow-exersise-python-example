# sum of first n prime numbers
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sum_of_first_n_prime_numbers(n):
    sum = 0
    count = 0
    i = 1
    while count < n:
        if is_prime(i):
            sum += i
            count += 1
        i += 1
    return sum

# sum_of_first_n_prime_numbers input int
n = int(input("Enter n: "))
print(sum_of_first_n_prime_numbers(n))