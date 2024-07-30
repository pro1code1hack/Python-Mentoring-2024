"""
### Task 1: Methods
**Objective**:
1. Create two sets, `A` and `B`, where `A` contains numbers from 1 to 10 and `B` contains numbers from 5 to 15.
2. Perform the following operations and print the results:
3. Find the union of `A` and `B`.
4. Find the intersection of `A` and `B`.
5. Find the difference between `A` and `B`.
6. Find the symmetric difference between `A` and `B`.
7. Add a new element 16 to set `B` and remove element 5.
8. Check if `A` is a subset of `B` and vice versa.
"""



A = set(range(1, 11))
B = set(range(5, 16))


union = A.union(B)
intersection = A.intersection(B)
difference = A.difference(B)
symmetric_difference = A.symmetric_difference(B)

# Modifying set B
B.add(16)
B.remove(5)

# Checking subset relationships
is_A_subset_B = A.issubset(B)
is_B_subset_A = B.issubset(A)

# Printing results
print("Union of A and B:", union)
print("Intersection of A and B:", intersection)
print("Difference of A and B:", difference)
print("Symmetric difference of A and B:", symmetric_difference)
print("Set B after adding 16 and removing 5:", B)
print("Is A a subset of B?", is_A_subset_B)
print("Is B a subset of A?", is_B_subset_A)






