#!/usr/bin/python3
import sys
# def factorial(n):
#     try :
#         if n<0 or type(n)!=int:
#             raise ValueError
#         else :
#             return factorial(n-1)*n
#     except ValueError:
#         print("value error")

# print(factorial(5))
try:
    sys.exit(1)
    print("try")
    
finally:
    print("finally")