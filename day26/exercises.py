numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

square_numbers=[number**2 for number in numbers]

print(square_numbers)


even_numbers=[num for num in numbers if num%2==0]
print(even_numbers)

with open("file1.txt") as file1:
    list1=file1.readlines()

with open("file2.txt") as file2:
    list2=file2.readlines()

new_list=[int(num.strip()) for num in list1 if num in list2]
print(new_list)
