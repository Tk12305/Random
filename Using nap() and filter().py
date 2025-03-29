nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
evens = list(filter(lambda X: X % 2 == 0, nums))

print(squared) # [1, 4, 9, 16, 25]
print(evens) # [2, 4]