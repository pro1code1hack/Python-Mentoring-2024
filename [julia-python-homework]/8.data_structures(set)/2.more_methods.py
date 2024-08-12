"""More Methods:"""

# Create three sets, X, Y, and K, with random numbers and some common elements among them.
# 2. Update set X with the intersection of X, Y, and K.
# 3. Perform a symmetric difference update between set Y and set K.
# 4. Check if X is now a subset of Y or K and print the result.
# 5. Convert set K into an immutable set and attempt to add another
# element to demonstrate the immutable property.

X = {3, 2, 54, 23, 66, 76, 4, 98, 94, 5, 87, 32, 7, 11, 423, 30, 845, 31, 68}
Y = {5, 25, 85, 125, 30, 66, 94, 48, 390, 23, 98, 13, 43, 65, 2, 45, 7}
K = {47, 71, 94, 5, 66, 48, 60, 74, 14, 23, 30, 7, 58, 25, 27}
print ("Intersection: ", X & Y & K)
print("Symmetric Difference Update, Y and K: ", Y.symmetric_difference_update(K))
print("X is a subset of Y: ", X < Y)
print("X is a subset of K: ", X < K)
immutable_set_K = frozenset(K)
print(immutable_set_K)

# Attempt to add an element
try:
    immutable_set_K.add(12)
except AttributeError as e:
    print(e)
