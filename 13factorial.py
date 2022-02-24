

def factorial(number):
    if not isinstance(number, int) or number < 0:
        print("N should be int and not negative...")
        return None
    if number in [0, 1]:
        return 1
    else:
        return number * factorial(number - 1)


if __name__ == '__main__':
    print(factorial(6))
    print(factorial(0))
    print(factorial(-2))
    print(factorial('string'))
