import re


def read_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

#task1
def match_ab(content):
    pattern = r'a*b*' 
    matches = re.findall(pattern, content)
    print( matches)

#task2
def match_ab23(content):
    pattern2 = r'ab{2,3}'
    matches2 = re.findall(pattern2 , content)
    print(matches2)


#task3
def find(content):
    pattern3 = r'[a-z]+_[a-z]+'
    matches3 = re.findall(pattern3 , content)
    print(matches3)

#task4
def upper_lower(content):
    pattern4 = r'[A-Z][a-z]'
    matches4 = re.findall(pattern4 , content)
    print(matches4)

#task5
def ending_b(content):
    pattern5 = r'a.*b$'
    matches5 = re.findall(pattern5 , content)
    print(matches5)

#task6
def replace(content):
    pattern6 = r'[,.]'
    matches6 = re.sub(pattern6 , ":" , content)
    print(matches6)

#task7
def snake_camel(content):
    matches7 = ''.join(word.capitalize() if i != 0 else word for i, word in enumerate(content.split('_')))
    print(matches7)

#task8
def split(content):
    pattern8 = r'(?=[A-Z])'
    result = re.split(pattern8 , content)
    print(result)

#task9
def spaces(content):
    result9 = re.sub(r'([a-z])([A-Z])' , r'\1  \2' , content)
    print(result9)

#task10
def camel_to_snake(content):
    result10 = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', content).lower()
    print(result10)




file_path = 'L5/row.txt'  


content = read_from_file(file_path)
match_ab(content)
print("1---------------------------------------")
match_ab23(content)
print("2---------------------------------------")
find(content)
print("3---------------------------------------")
upper_lower(content)
print("4---------------------------------------")
ending_b(content)
print("5---------------------------------------")
replace(content)
print("6---------------------------------------")
snake_camel(content)
print("7---------------------------------------")
split(content)
print("8---------------------------------------")
spaces(content)
print("9---------------------------------------")
camel_to_snake(content)
