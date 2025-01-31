
#task1
def gramsounes(grams):
    return grams / 28.3495231
grams = float(input())
print(gramsounes(grams))

# #task 2
def fahrenheit(temp):
    return  (5 / 9) * (temp - 32)
temp = float(input())
print(fahrenheit(temp))

# #task 3
def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    return chickens , rabbits

numheads = 50
numlegs = 140
chickens , rabbits = solve(numheads , numlegs)
print(chickens , rabbits)

# #task 4
def isprime(num):
    if num < 2:
     return False
    for i in range(2 , int(num**0.5) + 1):
       if num % i == 0:
          return False
    return True  
def filter_prime(numbers):
    return [num for num in numbers if isprime(num)]

num = list(map(int , input().split()))
print(filter_prime(num))


#  #task 5
from itertools import permutations
def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

s = input()
result = string_permutations(s)
print(result)

#task 6
def reversed(string):
    return ' '.join(string[ : : -1]) 
string = input().split()
print(reversed(string))

#task 7
def has_33(nums):
    for i in range(len(nums)):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
       
    return False
nums = list(map(int , input().split()))
print(has_33(nums))

#task 8
def spy_game(nums):
    code = [0 , 0 , 7]
    code_index = 0
    for num in nums:
        if num == code[code_index]:
            code_index += 1

        if code_index == len(code):
            return True
    return False
        





nums = list(map(int , input().split()))
print(spy_game(nums))

#task 9
def foundvolume(radius):
     pi = 3.141592653589793
     return 4/3 * pi * (radius ** 3)
radius = int(input())
print(foundvolume(radius))

#task 10
def unique(nums):
    uni = []
    for elements in nums:
        if elements not in uni:
            uni.append(elements)
    return uni

nums = list(map(int , input().split()))
print(unique(nums))

 #task 11  
def is_palindrome(sentence):
  obratno = sentence[ : : -1]
  if sentence == obratno:
    return True
  else:
    return False
  
sentence = input()
print(is_palindrome(sentence))


#task 12   
def histogram(nums):
    for num in nums:
        print('*' * num)

nums = list(map(int, input().split()))
histogram(nums) 

#task 13
import random

def guess_num():
    howmuch_guess = 0
    num_random = random.randint(1, 20)
    
    name = input("Hello! What is your name?\n") 
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    while True:
        guess = int(input("Take a guess.\n"))  
        howmuch_guess += 1  
        
        if guess < num_random:
            print("Your guess is too low.")
        elif guess > num_random:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {howmuch_guess} guesses!")
            break  


guess_num()


