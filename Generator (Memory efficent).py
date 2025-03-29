def square_numbers(n):
 for i in range(n):
  yield i ** 2

gen = square_numbers(5)
print(list(gen))  #[0, 1, 4, 9, 16]