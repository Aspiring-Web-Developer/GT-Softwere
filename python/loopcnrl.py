# LOOPCONTROL - break(terminte the loop), continue(skip the particular iter), pass(simply mention to avoid errors)

# for i in range(1,10):
#     if i ==2:
#         break
#     print(i)



# for i in range(1,10):
#     if i ==2:
#         continue
#     print(i)


# for i in range(1,10):
#     if i ==2:
#         pass
#     print(i)


num=12
is_prime=True

for i in range(1,num):
    if num%i==0:
        is_prime=False
        break

print(is_prime)
