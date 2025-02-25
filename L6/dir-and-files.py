#task1

from pathlib import Path
def list(path):
    p = Path(path)
    directories = [d.name for d in p.iterdir() if d.is_dir()]
    files = [f.name for f in p.iterdir() if f.is_file()]
    all_items = [a.name for a in p.iterdir()]
    return directories , files , all_items

path = "."

print(list(path))
print("---------------------------------------")

#task 2

import os
def checking(path):
    print("Existence: " , os.path.exists(path))
    print("Readble: " , os.access(path , os.R_OK))
    print("Writeble: " , os.access(path , os.W_OK))
    print("Executable: " , os.access(path , os.X_OK))

path = "."
checking(path)
print("---------------------------------------")

#task 3
def checking_exist(path):
    if os.path.exists(path):
        abs_path = os.path.abspath(path)
        print(os.path.dirname(abs_path))
        print(os.path.basename(abs_path))
    else:
        print("The path doesn't exists")
path = "."
checking_exist(path)

#task 4
with open("File_txt" , "w") as  file:
    file.write("Hello everyone , how is your week going?\n")
    file.write("We are good , thank you")
   


def count_lines (filename):
    with open(filename , "r") as file:
        lines = file.readlines()
        return len(lines)
    
filename = "File_txt"
print(count_lines(filename))

# task 5
list = ["Korea" , "Kazakhstan" , "Turkey" , "Brazil"]
with open("countries" , "w") as file:
    for country in list:
        file.write(country + "\n")

#task 6
import string
for lett in string.ascii_uppercase:
    fname = f"{lett}.txt"
    with open(fname , "w") as file:
        file.write("Hello")


#task 7
with open("tasksfrom" , "w") as fr:
    fr.write("This is simple text")

def copy(tasksfrom , tasksto):
    with open("tasksfrom" , "r") as fr:
        with open("tasksto" , "w") as to:
            to.write(fr.read())
    
copy("tasksfrom" , "tasksto")

#task 8
import os

with open("Txtfile" , "w") as file:
    file.write("Salem")




def delete_file(path):
    if os.path.exists(path):
        if os.access(path , os.W_OK):
            os.remove(path)
            print(f"File {path} has been deleted successfully.")
        else:
            print(f"File {path} does not exists ")

path = "Txtfile"
delete_file(path)