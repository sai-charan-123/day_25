#reduce(from functools import reduce())
def feb(x,y):
	return x*y
n=int(input("enter the number :"))
x=reduce(feb,range(1,n+1))
print(x)