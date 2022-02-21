

def power_of_two(n):
    counter = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            counter += 1
        else:
            return False, None
    return True, counter


if name == "main":
    for i in ([1, 2, 64, 1024, 3]):
        print(f'Is {i} power of two: ', power_of_two(i))
        
