#1)odd-even using while loop 

while True:
    number=int(input("Eenter a number"))
    if number %2==0:
         print("Number is even")
    else:
        print("Number is odd")

Output:
Eenter a number 2
Number is even 
Eenter a number 3
Number is odd  
Eenter a number



#2) using while
* 
* *
* * *
* * * *
* * * * *

Ans:
a=1
while a<=5:
    print('*'*a)
    a+=1


Output:
*
**
***
****
*****

#3) creat list 1-20 numbers list using while loop=> [1,2,3... 20]

Ans:
numbers_list = []
a = 1
while a <= 20:
    numbers_list.append(a)
    a += 1

print(numbers_list)

Output:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


#4)  creat list 20-1 (revers order) using while loop=> [20,19...1]

Ans:

numbers_list = []
num = 20
while num >= 1:
    numbers_list.append(num)
    num -= 1

print(numbers_list)

Output:[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#5) try with one any eg. break, contnue , pass control statement

Ans:

break...

for i in range(1, 6):
    if i == 5:
        break  
    print(i)

Output:
1
2
3
4

continue...

for i in range(1, 6):
    if i == 2:
        continue  
    print(i)

Output:
1
2
4
5

pass....

for i in range(1, 6):
    if i == 2:
        pass  
    else:
        print(i)
Output:
1
3
4
5










