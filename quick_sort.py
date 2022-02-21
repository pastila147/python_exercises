from random import randint


def quicksort(a):
    if len(a) <= 1:
        return a

    smaller, equal, larger = [], [], []
    pivot = a[randint(0, len(a)-1)]
    for i in a:
        if i < pivot:
            smaller.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            larger.append(i)

    return quicksort(smaller) + equal + quicksort(larger)


if __name__ == '__main__':
    unsorted = [23, 65, 1, 102, 72, 9]
    print(quicksort(unsorted))