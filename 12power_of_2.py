

def power_of_two(n):

    counter = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            counter = counter + 1
        else:
            return False
    print("n power of two: True")
    return counter


if __name__ == "__main__":
    print('power: ', power_of_two(8))
