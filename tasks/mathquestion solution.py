##1 question
##first methods for recursion
n=int(input("enter the number"))
def sum(n):
    y=0
    x=2
    for i in range(1, n+1):
        if n==1:
            y=y+1/(x)**1
        elif(n>=2):
            y=y+1/(x)**i
        else:
            return sum(n-1)+1
    print(y)

sum(n)

##second methods

n=int(input("enter the no"))
sum=0
x=2

for i in range(1, n+1):
    sum=sum + 1/x **i

print(sum)


##2question

n=int(input("enter the number"))
m=[]
for i in range(1, n+1):
    if i%2==0:
        u=i**2-1
        m.append(u)
    else:
        u=i**2+1
        m.append(u)

print(m)


##3question

def solve(a,b,x,y):
    m=(x+1/(y)**a) *(x-1/(y)**b)
    n=(y-1/(x)**a) * (y-1/(y)**b)
    q=m%n
    return q
a=int(input("enter the number of a"))
b=int(input("enter the number of b"))
x=int(input("enter the number of x"))
y=int(input("enter the number of y"))

print(solve(a,b, x,y))
