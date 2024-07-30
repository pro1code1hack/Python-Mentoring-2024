"""Methods: """
# 1. Create two sets, A and B, where
# A contains numbers from 1 to 10 and B contains numbers from 5 to 15.

# 2. Perform the following operations and print the results:
# 3. Find the union of A and B.
# 4. Find the intersection of A and B.
# 5. Find the difference between A and B.
# 6. Find the symmetric difference between A and B.
# 7. Add a new element 16 to set B and remove element 5.
# 8. Check if A is a subset of B and vice versa.

A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
B = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

print("Union: ", A | B)
print("Intersection: ", A & B)
print("Difference: ", A - B)
print("Difference: ", B - A)
print("Symmetric Difference: ", A ^ B)

B.add(16)
B.discard(5)
print("new B: ", B)
print("A in a subset of B: ", A < B)
print("B in a subset of A: ", B < A)
