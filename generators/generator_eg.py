def square_numbers(nums):
    for i in nums:
        print(f'num - {i}')
        yield(i**2)


squares = square_numbers([1, 2, 3, 4, 5])

# squares = (x*x for x in [1, 2, 3, 4, 5])

# print(squares)

for i in range(5):
    print(f'calling next for {i+1}')
    print(next(squares))
