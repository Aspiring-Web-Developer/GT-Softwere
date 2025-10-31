# input="Search Google or type a URL"
# splitit=input.split()
# print(splitit)
# divide=splitit[:2]
# print(divide)
# empty=[]
# for n in divide:
#     reversed_list=n[::-1]
#     join=empty.append(reversed_list)
# print(empty)


# divide2=splitit[2:]
# print(divide2)

# for n in divide2:
#     reversed_list=n[::-1]
    
#     join=empty.append(reversed_list)

# print(empty)


# folder=" ".join(empty)
# print(folder)




letter="search Google or type a URL"
split=letter.find("or")

value1=letter[:split]
value2=letter[split:]

reve1=value1[::-1]

reve2=value2[::-1]

result=f"{reve1} {reve2}"
print(result)