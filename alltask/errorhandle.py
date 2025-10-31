# 1ï¸âƒ£ ZeroDivisionError
# ðŸ”¹ Write a program that asks the user to enter a number and divides 100 by it.
# ðŸ‘‰ Handle the case where the number entered is 0.

# 2ï¸âƒ£ ValueError
# ðŸ”¹ Ask the user to enter an integer.
# ðŸ‘‰ Handle the case where the user enters a string like "abc".

# 3ï¸âƒ£ IndexError
# ðŸ”¹ Create a list of 3 elements. Try to access an index that doesnâ€™t exist (e.g., index 10).
# ðŸ‘‰ Handle the error gracefully.

# 4ï¸âƒ£ KeyError
# ðŸ”¹ Create a dictionary with keys 'name' and 'id'.
# ðŸ‘‰ Try accessing a key 'email' that does not exist and handle the error.

# 5ï¸âƒ£ TypeError
# ðŸ”¹ Try to add a string and a number together (e.g., "100" + 50).
# ðŸ‘‰ Handle the error and fix it.

# num=int(input("Eter the number"))
# num1= 100


# try:
#    num3=num1/num
#    print(num3)
# except ZeroDivisionError:
#     print("the second number shouldn't give zero")
# except Exception as e:
#     print(e)



# try:
#     num=int((input("ENter the number")))

#     print(num,"you give the number")
# except ValueError:
#     print("you shouldn't type the number")
# except Exception as e:
#     print(e)


# number=[10,50,70]
# try:
    
#     print(number[6])
   
# except IndexError:
#     print("This index not available in the list")
# except Exception as e:
#     print(e)

# detail={
#     'name':'deepak',
#     'ID':453
# }



# try:
#    print(detail['email'])
# except KeyError:
#     print("key doesn't exit")
# except Exception as e:
#     print(e)

try:
    num1=input("Enter The Num")
    num2=int(input("enter the num"))
    print(num1+num2)
except TypeError:
    print("This cound't add this values")
except Exception as e:
    print(e)