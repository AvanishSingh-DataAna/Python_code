'''
li = ['nitin','anurag','abhisek', 'xyzmnyx']
mi = []
for i in li:  #anurag
    if i[0]==i[-1] and i[1]==i[-2]:
        mi.append(i)
print(mi)
      

li = ['nitin','anurag','abhisek', 'xyzmnyx','nitin']

for i in li:# xyzmnyx
    d = []
    mi = []
    for j in i: #y
        if j not in mi:  #F
            mi.append(j)
        else:
            d.append(j)
    #print(mi)   
    print(f'duplicat elements of {i} is:{d}')



for i in range(5,51,5):
    print(i)



t = int(input("Enter number:"))
for i in range(1,11):
    print(f'{t}x{i}={t*i}')




for i in range(5,21):
    for j in range(1,11):
        print(f'{i}*{j}={i*j}')
    print("--------------------------------------------")
        

num = int(input("Enter a number:"))
for i in range(2,num+1):
    if num%i==0:
        print(i)


num = int(input("Enter a number:"))
li = []
for i in range(2,num+1):
    if num%i==0:
        li.append(i)
print(li)
        

li = [22,95,63,100,56]
for i in li:
    mi = []
    for j in range(2,i+1//2):
        if i%j==0: #T
            mi.append(j)
print(f'factors of {i} are:{mi}')




li = [100,300,350, 400,230,700, 900]
x = []
y = []
for i in range(len(li)):#6
    if i%2==0:
        x.append(li[i])
    else:
        y.append(li[i])

print("Even Turms are:",x)
print("Odd Turms Are:",y)





li = [100,300,350, 400,230,700, 900]
x = []
y = []
for i in range(0,7,2):
    x.append(li[i])
for j in range(1,7,2):
    y.append(li[j])
    
print(x)
print(y)



s = 'Hello avanish Singh How are You'
c = 0
index = -1
for i in s:
    index = index+1
    if i=='o':
        c = c+1 #c=1
        if c==2:
            print(index)


a = input("Enter What charcter index you want:")
s = 'Hello avanish Singh How are You'
c = 0
index = -1
for i in s:
    index = index+1
    if i==a:
        c = c+1 
        if c==2:
            print(index)


p = int(input("How Many people you are:"))
f = input("How Was Your experience:")
b = input("Do You Want to give us Some Tip (y/n):")
bill = 1200
if b=='y':
    t = int(input("How much you want to give:"))
    bill = bill+t
    print("Your New Bill is:",bill)
    print(f'Each of You have to pay:{bill/p}')
else:
    print("Thank You For Visiting, you bill is:",bill)
    print(f'Each of You have to pay:{bill/p}')
        


# factorial numbers-:
# n!=  n*(n-1)!
# 5 = 5*4! = 5*4*(4-1)! = 5*4*3*2*1 = 120
# 6! = 6*5*4*3*2*1 = 720

num = int(input("Enter any number:"))#5
f = 1
for i in range(num, 0,-1):  #(5,4,3,2,1)
    f = f*i  #1*5 = 5*4 = 20*3 = 60*2 = 120*1 = 120
print('factorila result is:',f)
    


# prime number

# 37-:  
# 25-:

num = int(input("Enter any number:")) #12
for i in range(2, num):
    if num%i==0:
        print("Your Number is NoT prime Number")
        break
else:
    print("Your number is prime")
    


num = int(input("Enter any number:")) #12
if num>0:
    for i in range(2, num):
        if num%i==0:
            print("Your Number is NoT prime Number")
            break
    else:
        print("Your number is prime")
else:
    print("Wrong Input")
    





for i in range(100,201):
    for j in range(2, i):
        if i%j==0:
            break
    else:
        print(i, end=',')




# fabnacci series

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...................

turm = int(input("Enter The Number of turms You want:")) #10
f = 0
s = 1
for i in range(turm): #10-:(0,1,2,3,4,5,6,7,8,9)
    print(f,end=',')
    temp = f  #temp=5
    f = s     #f = 8
    s = s+temp # s = 13
    
#0,1,1,2,3,5,8, ..............................  



    


# pattern programming

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

num = int(input("Enter Number of Rows:"))#6
for row in range(1, num+1):#(1,2,3,4,5,6)
    for col in range(1,row+1): #(1,2,3,4)
        print(col, end=' ')
    print()
              
    

   
    
num = int(input("Enter Number of Rows:"))#6
for row in range(1, num+1):#(1,2,3,4,5,6)
    for col in range(1,row+1): #(1,2,3,4)
        print('#', end=' ')
    print()    




# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

num = int(input("Enter Number of Rows:"))#6
for row in range(1, num+1):#(1,2,3,4,5,6)
    for col in range(1,row+1): #(1,2,3,4)
        print(row, end=' ')
    print()    



num = int(input("Enter Number of Rows:"))
n = 1
for row in range(1, num+1):
    for col in range(1, row+1):
        print(n, end=' ')
        n = n+1
    print()
        

name = input("Enter What You want:") #python
for row in range(len(name)):  #(0,1,2,3,4,5)
    for col in range(row+1):
        print(name[col],end=' ')
    print()



# enumerate(list)

clrs = ['red','blue','green','yellow','black','red', 'green']
for i,j in enumerate(clrs):
    print(i,'-->',j)




clrs = ['red','blue','green','yellow','black','red', 'green']
for i,j in enumerate(clrs):
    print(i+1,'-->',j)


import math
for i,j in enumerate(dir(math)):
    print(i+1,'.',j)



i = 1
while(i<=10):
    print(i)
    i +=1


num = int(input("Enter a number:"))
i = 1
f = 1
while(num>=i):
    f = f*i
    i = i+1
print(f)



x = 22
if x>=18:
    pass    
print(x)



s = input("Enter a string")
for i in s:
    if i=='a':
        continue
    else:
        print(i,end='')



s = input("Enter a string") # avanish
i = 0
while(i<len(s)):
    if s[i]=='a':
        i = i+1
        continue
    else:
        print(s[i],end='')
        i = i+1
        
        

s = input("Enter your string") # avanish
c = 0
for i in s:
    if i=='a':#T
        c = c+1 #2
        if c>1:
            continue
        else:
            print(i, end='') # a
    else:
        print(i,end='')  #v           
    
    
s = input("Enter a string") # avanish
i = 0
c = 0
while(i<len(s)):
    if s[i]=='a':
        c = c+1
        if c>1:
            i = i+1
            continue
        else:
            print(s[i],end='')
            i = i+1     
    else:
        print(s[i],end='')
        i = i+1



# var = [result for loops if condtions]
x = [12,56,43,67,88,97,13,15,20,40]
res = [i for i in x if i%2==0]
print(res)
print([i for i in x if i%2==0])
[print(i) for i in x if i%2==0]



x = [5,35, 90, 66, 65, 70]
print([i for i in x if i%5==0 if i%7==0])



'''
clrs = ['red', 'blue', 'green', 'mango', 'pink', 'cyan']
res = [i for i in clrs if 'e' in i]
print(res)


clrs = ['red', 'blue', 'green', 'mango', 'pink', 'cyan']
res = [i for i in clrs for j in i if  ]
print(res)
















































            
    
    
    
    

    
    





































