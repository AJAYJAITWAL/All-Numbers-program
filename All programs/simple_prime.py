# simple prime number

n = int(input("Enter the no: "))
count = 0
i=1
while i<=n:
	if n%i==0:
		count+=1
	i+=1

if count==2:
	print("Pime number")
else:
	print("Not a prime number")