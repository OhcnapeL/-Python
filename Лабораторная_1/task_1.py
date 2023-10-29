numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

sum_of_num = sum(numbers[:4]) + sum(numbers[5:])
count_of_num = len(numbers)
average_of_num = sum_of_num / count_of_num
numbers[4] = round(average_of_num, 2)

print("Измененный список:", numbers)
