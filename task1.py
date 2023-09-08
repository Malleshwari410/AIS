Q1) grade code
p=50
O: p>75
A : 60 < p>75
B: 50<p<60
C: 35<p<50
fail:p<35

Ans-

p = 70
if p > 75 :
    print("grade: O")
elif 60 < p <= 75 :
     print("grade: A")
elif 50 < p <= 60 :
     print("grade: B")
elif 35 > p <= 50 :
     print("grade: C")
else:
    print("grade:fail")

Output : grade: A


***********************************************************

Q2)n divisible by 2 or 3
n=7
2 divisble, 3 not
divisible by 2,and 3
divisible by 3, not 2
not divisible by 2, and 3

Ans-

n = 7
if n%2==0 and n%3!=0:
    print("n is divisible by 2")
elif n%3==0 and n%2==0:
    print("n is divisible by 2 and 3")    
elif n%3==0 and n%2!=0:
    print("n is divisible by 3")  
else:
    print("n is not divisible by 2 and 3")      

Output- n is not divisible by 2 and 3


***********************************************************

Q3) print odd value between 20 and 80, without using if. Using for loop only

Ans-

for i in range(21,81,2):
    print(i)
    
**************************************************************************

Q4)creat a list of 1 to 20 number using for loop [1,2,3..20]

Ans-

numbers = []
for i in range(1,21):
    numbers.append(i)
print(numbers)    

**************************************************************************

Q5)create a  list of 20 to 1 value using  for loop (don't Use Reverse)
[20,19,18,...3,2,1]

Ans-

num=[]
for i in range(20,0,-1):
    num.append(i)
print(num)    

**************************************************************************
Q6)take Cube of odd values between 20 to 40

Ans-


for i in range(20,40):
    if i%2!=0:
        print(i**3)
        
**************************************************************************
 
 Q7)take 5 freinds name in list name=[a,b,c,d,e]
take corresponding ages in second list age = [20,21,23,25,24]
expected ans:
    my name is a , my age is 20
    my name is b, my age is 21
    .
    .

Ans-

names=["a","b","c","d","e"]
age=[20,21,22,23,24]
for i in range(len(names)):
    print("My name is",names[i],"My age is",age[i])
    
**************************************************************************

Q8)Solve Using if and for loop  and data types methods ; 

Given a list, write a Python code  to swap first and last element of the list.

Ans-
a=[10,20,30,40,50]
l=len(a)
a[0],a[-1]=a[-1],a[0]
print(a)

*************************************************************************************

Q9)write code count lenght of string

Ans-

a=sorted("malleshwari")
print(len(a))

*************************************************************************************

Q10)Write a Python program to get the sum of a only non-negative integer. ex, [1,4,-5,-20,10] ans is 15

Ans-

a=[1,4,-5,-20,10]
total=0
for i in range(0,len(a)):
    if a[i]>0:
      total=total+a[i]
print(total)  

**************************************************************************************

Q11)write code of factorial , ex.ans 6 (3*2*1)

Ans-

num=int(input("enter a number :"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)

**************************************************************************************
     

