
def digit_sum(n):
    # Base case
    if n == 0:
        return 0

    # Recursive case
    return (n % 10) + digit_sum(n // 10)


number = int(input())

print(digit_sum(number))
