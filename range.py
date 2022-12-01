'''
DATE=30th NOV 2022
DAY= wednesday
TOPIC=range
AUTHOR= nikhil
'''
v=1,2,3,4,5
print(v) #(1,2,3,4,5)
print(*v) #1 2 3 4 5
a=range(10)
print(a) #range(0, 10)
p=10,20,30
for i in p:
  print(i) #10 20 30(vertically)
for i in range(5):
  print(i) #0 1 2 3 4(vertically)
 k=int(input('enter the value of k:'))
for i in range(1,k+1):
  print(i,end='\n') #1 2 3 4 5 6 7 8  9 10(vertically)
for i in range(1,40,2):  
  print(i,end=" ") #1 3 5 7 11 13 17 19 21 23 25 27 29 31 33 35 37 39(horizontally)
for i in range(2,40,2):
  print(i,end=' ')#2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38
for i in range(10,0,-1):
  print(i,end=' ') #10 9 8 7 6 5 4 3 2 1
l=int(input('enter the value of l:'))
for i in range(10,-1,-1):
  print(i)  #10 9 8 7 6 5 4 3 2 1 0(vertically)
u=[2,2.0,'pk']
for i in u[::-1]:
  print(i)  #pk 2.0 2(vertically)
  u='nikhilpaspuleti'
for i in u[::3]:
  print(i,end=' ')  #k s a o
n=int(input('enter the value of n:'))
for i in range(n):
 print(i) #0to9 vertically
n=int(input('enter any integer number:'))
for i in range(25,n):
  print(i)  #25 to 30 vertically
n=int(input('enter any integer number:'))
for i in range(2,n,2):
  print(i)  #2 4 6 8
int(f'{n} odd number')
