#Write a Python function to find the maximum of from given
def max_number(a):
    for i in a:
        return max(a)
a=[42,35,78,17,35,97,36,0,25]
max_number(a)

***************************************************************************************************************

#Write a Python function to sum all the numbers in a list. Sample List : [8, 2, 3, 0, 7] Expected Output : 20
def add_list(a):
    b=0
    for i in range(len(a)):
        b=b+a[i]
    print(b)
a=[8,2,3,0,7]
add_list(a)


***************************************************************************************************************


# Write a Python function that takes a list and returns a new list with distinct elements from the first list.  
#Sample List : [1,2,3,3,3,3,4,5] Unique List : [1, 2, 3, 4, 5]
def get_unique_elements(input):
    uniquelist = []
    for item in input:
        if item not in uniquelist:
            uniquelist.append(item)
    return uniquelist

samplelist = [1, 2, 3, 3, 3, 3, 4, 5]
uniquelist = get_unique_elements(samplelist)
print(uniquelist)


***************************************************************************************************************


#Write a Python function total number of Combinations
from itertools import combinations as c

def combo(a,n):
    a=c(a,n)
    for i in a:
        print(i)
s="malleshwari"
combo(s,3)


***************************************************************************************************************

#Write a Python function total number of permutation
from itertools import permutations as p

def per(a):
    b=p(a)
    for i in b:
        print(i)
a=(6,5,4)
per(a)


***************************************************************************************************************

#Define a function which counts vowels and consonant in a word.
def vowel_count(n):
    count = 0
    count1 = 0
    vowel = set("aeiouAEIOU")
    for alphabet in n:
        if alphabet in vowel:
            count = count + 1
        elif alphabet not in vowel:
            count1=count1+1
     
    print("count of vowels :", count)
    print("count of consonant :", count1)
n=input("enter what you want : ")
vowel_count(n)


***************************************************************************************************************

#Define a function that accepts lowercase words and returns uppercase words.
def upper_case(a):
    print(a.upper())
a=input("enter what you want : ")
upper_case(a)


***************************************************************************************************************

# count lower case and upper case letter.
def count_letters(a):
  count = 0
  count1 = 0
  for letter in a:
    if letter.islower():
       count += 1
    elif letter.isupper():
      count1 += 1
  return count,count1


a=input("enter what you want : ")
x,y=count_letters(a)
print("upper case latter in your typing is : ",y)
print("lower case latter in your typing is : ",x)

