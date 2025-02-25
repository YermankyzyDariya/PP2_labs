import math

#task 1
a = [4 , 5 , 7]
multip = math.prod(a)
print(multip)

#task 2
def count(str):
    upper = sum(1 for char in str if char.isupper())
    lower = sum(1 for char in str if char.islower())
    return upper , lower
str = "Hello worlD"
print(count(str))

#task 3

def is_palindrome(s):
    return list(s) == list(reversed(s))
s = "MadaM"
print(is_palindrome(s))

#task 4
import time

def delayed_sqrt(num, delay):
    time.sleep(delay / 1000) 
    return math.sqrt(num)


num = 25100
delay = 2123  

result = delayed_sqrt(num, delay)
print(f"Square root of {num} after {delay} milliseconds is {result}")

#task 5
tp = (1 , True , [9 , 17])
if all(tp) == True:
    print("True")
else:
    print("False")