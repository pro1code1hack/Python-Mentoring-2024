"""Enhance the provided code to perform the following actions on a given list:"""

# • Display the length of the list.
# • Print the sum, max, min and the average.
# • Print the last element of the list.
# • Output the list in reverse order (remember to use slicing).
# • Print "YES" if the list contains the numbers 4 and 9, and "NO" otherwise.
# • Show the list with the first and last elements removed (create a new list object instead).
# • Print the third element from the end of the list.
# • If the second element is > 10, replace it with 10.


numbers = [3, 12, 5, 8, 4, 9, 15, 22]

len_of_list = len(numbers)
print("Length: ", len_of_list)

summary = sum(numbers)
print("Summary: ", summary)

max_num = max(numbers)
print("Max: ", max_num)

min_num = min(numbers)
print("Min: ", min_num)

avg = round(summary / len_of_list)
print("Average: ", avg)

copy_num = numbers[:]
last_num = copy_num.pop()
print("Last element: ", last_num)

copy_num = numbers[:]
reversed_list = copy_num[::-1]
print("Reversed list: ", reversed_list)

if 4 in numbers and 9 in numbers:
    print("YES")
else:
    print("NO")

third_from_end = numbers[-3]
print("Third element from the end ", third_from_end)

if copy_num[1] > 10:
    copy_num.pop(1)
    copy_num.insert(1, 10)
print("List after changind the 2nd element: ", copy_num)

## Why
## C0103: Constant name "len_of_list" doesn't conform to UPPER_CASE naming style (invalid-name)
## C0103: Constant name "third_from_end" doesn't conform to UPPER_CASE naming style (invalid-name)
## but other names are ok?
