# perfact number program

n=int(input("enter the no"))
sum=0
p=n
while n>0:
	rem = n%10
	sum=sum+rem
	n//=10
if p==sum:
	print("No is perfact")
else:
	print("No is not perfact")