class check_palindrome():
	

	def is_palindrome(self,val):
		rev=str(val)[::-1]
		if int(val) == int(rev):
			print ("Nearest Palindrome is:", val)
			return True

	def inputs(self,input):
		input1=input
		input2=input
		while input !=0:
			if self.is_palindrome(input1) or self.is_palindrome(input2):
				break
			input1=int(input1)+1
			input2=int(input2)-1

run=check_palindrome()
x=input("Enter a number:")
run.inputs(x)