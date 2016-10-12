


def is_palindrome(n):
    str_n = str(n)
    rev_n = str_n[::-1]
	
    if str_n == rev_n:
        return True
    else:
        return False


number = int(raw_input("Enter a number : "))
check_n = number
while True:
    palindrome = is_palindrome(check_n)
    if palindrome:
        print "The next palindrome number is %s"%check_n
        break
    else:
        check_n = check_n + 1
