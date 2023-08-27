#print("hello world")
import random
print("welcome to my password generator!")
num_of_letter=input("how many letters you want in a password\n")
num_of_letter=int(num_of_letter)
num_of_symbols=input("how many symbols you need in a password\n")
num_of_symbols=int(num_of_symbols)
num_of_numbers=input("how many numbers you need in a password\n")
num_of_numbers=int(num_of_numbers)
letters = ['a','b','c','d','e','f','A','B','C','D','E','F']
symbols = ['!','@','#','$','%','^','&']
numbers = ['1','2','3','4','5','6','7','8','9','0']


my_password=''
for will in range(num_of_letter):
    select_letter=random.choice(letters)
    my_password=my_password+select_letter

for qwerty in range(num_of_symbols):
    select_symbols=random.choice(symbols)
    my_password=my_password+select_symbols


for will in range(num_of_numbers):
    select_numbers=random.choice(numbers)
    my_password=my_password+select_numbers

print(my_password)
