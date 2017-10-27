# # factorial program using recrusion
def fact(n):
	if n==0:
		return 1
	return n * fact(n-1)
print(fact(5))

# factorial program without recrusion
def fact(n):
	num=n
	while num != 1:
		n=n * (num-1)
		num=num-1
	return n
print(fact(5))
