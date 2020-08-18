# write a program to calculate prime no in the interval of lower to upper and also find every element sum is 10

lower=int(input("Enter the lower no"))
upper=int(input("Enter the upper no"))

for i in range(lower,upper+1):
	if i>1:
		for j in range(2,i):
			if i%j==0:
				break
		else:
			print(i)
			sum=0
			while i>0:
				s=i%10
				sum=sum+s
				i=i//10
			if sum==10:
				print(sum)