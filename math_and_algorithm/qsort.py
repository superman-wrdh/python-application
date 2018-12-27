# -*- encoding: utf-8 -*-


def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        return qsort([i for i in arr[1:] if i < pivot]) + [pivot] + qsort([i for i in arr[1:] if i > pivot])


def qsort2(arr):
    if len(arr) <= 1:
        return arr
    else:
        less = []
        pivot = []
        more = []
        p = arr[0]
        for i in arr:
            if i < p:
                less.append(i)
            elif i > p:
                more.append(i)
            else:
                pivot.append(i)
        return qsort(less) + pivot + qsort(more)


if __name__ == '__main__':
    a = [1, 3, 5, 7, 9, 1, 6, 2, 2, 8]
    b = [1, 3, 5, 7, 9, 1, 6, 2, 2, 8]
    c = [1, 3, 5, 7, 9, 1, 6, 2, 2, 8]
    d = [1, 3, 5, 7, 9, 1, 6, 2, 2, 8]
    print(sorted(c))
    print(qsort(a))
    print(qsort2(d))
