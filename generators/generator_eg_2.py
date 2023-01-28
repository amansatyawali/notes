def print_num():
    print('a')
    print('a')
    yield 1
    print('b')
    print('b')
    yield 2
    print('c')
    print('c')


gen_obj = print_num()


print(gen_obj)
print(next(gen_obj))
print('First print statement ran')
print(next(gen_obj))
print('Second print statement ran')
print(next(gen_obj))
