def simple_gen():
    for i in range(5):
        yield i  # pause here, return value, resume next time
        # return i

gen = simple_gen()
print(gen)

print(next(gen))

print(next(gen))

print(next(gen))



# print(next(gen))  # 0
# print(next(gen))  # 1
# print(list(gen))  # [2, 3, 4]