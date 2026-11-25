# Given:
# numbers = [1, 2, 3, 2, 4, 1, 5, 3]

# Create a new list containing only unique elements.

# Expected output:
# [1, 2, 3, 4, 5]

# Try to preserve the original order.

numbers = [1, 2, 3, 2, 4, 1, 5, 3]

unique = []

for i in numbers:

    if i not in unique:
        unique.append(i)


print(unique)