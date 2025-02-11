#task 1
def generates_squares(N):
    for i in range(N+1):
        yield i**2
N = int(input())
for sqr in generates_squares(N):
    print(sqr , end=" ")
#task 2
def generator_even(n):
   for i in range(0 , n+1):
       if i % 2 == 0:
           yield i
n =int(input())
for even in generator_even(n):
    print(even , end=" , ")
#task 3
def generator_divible(n):
    for i in range(0 , n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
for div in generator_divible(n):
    print(div , end=" ")
#task 4
def generator_square(a , b):
    for i in range(a , b+1):
        yield i ** 2
a = int(input())
b = int(input())
for sqrt in generator_square(a , b):
    print(sqrt , end=" ")
#task 5
def countdown(n):
    while n >=0:
        yield n
        n -= 1
n = int(input())
for num in countdown(n):
    print(num , end=" ")