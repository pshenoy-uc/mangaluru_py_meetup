num = int(raw_input("Enter the number : "))
num+=1
while True:
	str_num = str(num)
	rev_str = str_num[::-1]
	if(rev_str == str_num):
		print "It is a palindrome"
		print "Next Palindrome number ", rev_str	
		break
	else :
		num += 1
