

def bubble_sort(arr=None):
    if not arr:
        return list()

    n = len(arr)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == '__main__':
    l = [22, 1, 98, 45, 34, 84, 1, 6, 4]
    print(bubble_sort(l))