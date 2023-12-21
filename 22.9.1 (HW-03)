def binary_search(list_of_n,  single_n, left, right):
    if left > right:
            return False
    middle = (right + left) // 2
    if list_of_n[middle-1] < single_n and single_n <= list_of_n[middle]:
       return [middle-1]
    elif single_n < list_of_n[middle]:
         return binary_search(list_of_n, single_n, left, middle - 1)
    elif single_n == list_of_n[middle - 1]:
         return binary_search(list_of_n, single_n, left, middle - 1)
    else:
         return binary_search(list_of_n, single_n, middle + 1, right)
while True:
    try:
        list_of_n = list(map(float, input("\nВведите числовую последовательность: ").strip().split()))
        single_n = float(input('Ведите произвольное чило: '))
        if all(type(x) != float for x in list_of_n):
            print('Введенное значение должно быть числом')
        if type(single_n) != float:
            print('Введенное значение должно быть числом')
        break
    except ValueError:
       print('Введенное значение должно быть числом')
list_of_n.sort()
print(list_of_n)
left = int(list_of_n[0])
right = int(list_of_n[-1])
if single_n < left or single_n > right:
    print('Введенное число не попадает в список')
else:
    print(binary_search(list_of_n, single_n, 0, len(list_of_n) - 1 ))
