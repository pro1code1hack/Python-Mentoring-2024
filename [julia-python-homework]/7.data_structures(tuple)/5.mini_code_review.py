"""Updated hometasks:"""

# 6.8.validating_ip_address
address = input("Enter an IP-address: x.y.z.a: ")
int_in_address = tuple(int(char) for char in address.split("."))
if len(int_in_address) == 4:
    for num in int_in_address:
        if num < 0 or num > 255:
            print(f"The IP-address {address} is NOT valid")
            break
    else:
        print(f"The IP-adress {address} is valid")
else:
    print(f"The IP-adress {address} is NOT valid")

# 6.6.ascii_alphabet
alphabet_tuple = tuple(chr(num) for num in range(97, 123))
print("Alphabet is: ", alphabet_tuple)

# 6.4.average_of_evens
list_elements = input("Enter a list of numbers (separated by space): ")
tuple_even_num = tuple(int(char) for char in list_elements.split(" ") if int(char) % 2 == 0)
avg = round(sum(tuple_even_num) / len(tuple_even_num))
print("The average of even numbers is:", avg)

# 6.2.slicer_and_dicer
str_of_numbers = input("Enter a list of numbers (separated by space): ")
start_index = int(input("Enter start index for slicing: "))
stop_index = int(input("Enter stop index for slicing: "))
tuple_of_nums = tuple(int(char) for char in str_of_numbers.split(" "))
output = tuple_of_nums[start_index:stop_index]
print("The sliced tuple is: ", output)

# 6.5.list_of_numbers_operations
numbers = [3, 12, 5, 8, 4, 9, 15, 22]
numbers_tuple = tuple(numbers)

## using tuple
len_of_list = len(numbers_tuple )
print("Length: ", len_of_list)

summary = sum(numbers_tuple )
print("Summary: ", summary)

max_num = max(numbers_tuple )
print("Max: ", max_num)

min_num = min(numbers_tuple )
print("Min: ", min_num)

avg = round(summary / len_of_list)
print("Average: ", avg)

if 4 and 9 in numbers_tuple:
    print("YES")
else:
    print("NO")

third_from_end = numbers_tuple[-3]
print("Third element from the end ", third_from_end)

## using list
copy_num = numbers[:]
last_num = copy_num.pop()
print("Last element: ", last_num)

copy_num = numbers[:]
reversed_list = copy_num[::-1]
print("Reversed list: ", reversed_list)

if copy_num[1] > 10:
    copy_num.pop(1)
    copy_num.insert(1, 10)
print("List after changind the 2nd element: ", copy_num)
