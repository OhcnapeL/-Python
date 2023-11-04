numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index_none = 0

for index, value in enumerate(numbers):
    if value is None:
        index_none = index

sum_of_num = sum(numbers[:index_none]) + sum(numbers[index_none + 1:])
count_of_num = len(numbers)
average_of_num = sum_of_num / count_of_num
for i in range(len(numbers)):
    if numbers[i] is None:
        numbers[i] = average_of_num

print("Измененный список:", numbers)
