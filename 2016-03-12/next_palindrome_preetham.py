# nextPalindrome
# A Python program to find the next python Number from the given number.

num = int(raw_input("Enter the number: "))

while True:
	num_str = str(num)
	rev = num_str[::-1]

	if rev == num_str:
		print rev
		break

	num += 1
