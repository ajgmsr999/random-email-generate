
"""

email = ''
for _ in range(7):
    letter = random.sample(letters,1)[0]
    email += letter

email += '@gmail.com'
"""
"""

import random
import string

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

print (random_char(7)+"@gmail.com")
"""

import random
import string

#letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
         #  "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]
#Name = ["ss"]

#print=("Enter the Name create gmail account ")
"""

lname=["", "" ]
addn=random.choice(lname)
print (addn+"@gmail.com")
#random1 = random.choice(letters)

#for x in random1(7):
print ("Enter the Name for create gmail Account")


"""

'''
import random
import string

#char_num= ["name"]
firstname=("ml")
lastname=("student")
#print=("Enter the first name")

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


def gmail_create(char_num):

    
    return '' ''.join("ml"  "student")    

print (random_char(7)+"@gmail.com")

print (gmail_create(7)+"@gmail.com")


'''
'''
i want to make it so i get 7 random letters form my list and make it into a random email, however i can't get it to print out a full email only 1 letter at a time.

'''

'''

import random
import string

letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]

random1 = random.choice(letters)

for x in random1(7):
    print (random1 + "@gmail.com")
'''
import itertools
import random
#letters =  ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
          # "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]

#
# print("Enter the class name for gmail generate")
gen = input("Enter the randaom name to generate email :")

#print(gen)
#fn = ["ms"]
sclass  = [ "ml","1","2","3","4","5","6","7","8","9","10","11","12"]
add = (  sclass)
#school = ["ml","class","1","2","3","4","9","8"]
all_combos = list(itertools.combinations(add,2)) #make all 7 letter combinations
#all_combos = list(itertools.combinations(school,7)) #make all 7 letter combinations
all_combos = [gen.join(combo) for combo in all_combos] #make them strings
email = random.sample(all_combos,1)[0]+'@gmail.com' #grab a random one, add @gmail.com

#email1 = gen.sample(all_combos,1)[0]+'@gmail.com' #grab a random one, add @gmail.com
print(email)
'''

email = ''
for _ in range(7):
    letter = random.sample(school,1)[0]
   # email += letter
    #email += '@gmail.com'
'''
   
