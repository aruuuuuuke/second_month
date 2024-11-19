def binary_search(A, val):
    N = len(A)
    ResultOk = False
    pos = -1
    first = 0
    last = N-1
    while first < last:
        middle = (first + last) // 2
        if val == A[middle]:
            first = middle
            last = first
            ResultOk = True
            pos = middle
            break
        elif val > A[middle]:
            first = middle + 1
        else:
            last = middle - 1
    if ResultOk == True:
        print(f'Элемент найден на позиции: {pos}')
    else:
        print('Элемент не найден')


sps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
binary_search(sps, target)


def bubble_sort(numbers):
    for j in range(len(numbers)-1):
        chek = False
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                s = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = s
                chek =True
        if chek == False:
            break
    return numbers


spisok = [6, 8, 3, 6, 1, 9, 7, 1, 5, 4]
print(bubble_sort(spisok))
