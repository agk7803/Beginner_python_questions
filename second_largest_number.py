# Given:
# numbers = [10, 45, 20, 89, 67, 89, 34]

# Find the second-largest distinct number without using sort() or sorted().

# Expected output:
# 67

nums = [10, 45, 20, 89, 67, 89, 34]

second= 0
largest= 0

for i in nums:
    if i >largest:
        second=largest
        largest= i

    elif i <largest:
        if second == 0 or i >second:
            second = i

print(second)