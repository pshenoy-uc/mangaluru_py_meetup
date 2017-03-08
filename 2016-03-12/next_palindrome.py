"""
Author: K@rthik Bh@t K.
Date: March 14, 2016 11:23 AM

Description:
This code finds the next Palindrome number of the given number.
If given number itself is a palindrome, it will find next palindrome.

Python Style-Guide: PEP8
"""
def nextPalindrome(number):
    str_num = str(number)
    length = len(str_num)
    if length <= 1 and number != 9:
        return number+1
    if number == 9:
        return 11
    mid = length // 2
    if float(length) % 2 == 0:
        # if length of string is even do the following.
        # For example: number = 123456; rev_num = 123321
        rev_num = str_num[:mid] + str_num[mid-1::-1]
        if number >= int(rev_num):
            # Reverse the given number and check if the number is
            # Greater than or equal to the given number. If number is
            # greater than or equal i.e 123456 >= 123321
            # split by mid i.e Get the first part "123" and add one to it "124"
            # "palin = 124", reverse it i.e "palin[::-1] = 421"
            # reverse = 124421
            palin = str(int(str_num[:mid]) + 1)
            reverse = palin + palin[::-1]
            if len(reverse) > length:
                reverse = reverse[:mid] + reverse[mid+1:]
            return reverse
        else:
            # If number is less than rev_num i.e
            # For example: 123000 then reverse is 123321.
            return rev_num
    else:
        # If number has odd length then add the middle element
        # in the middle of the string. Example: 12345
        # rev_num = "12" + "3" + "21"
        # import pdb; pdb.set_trace()
        upto_mid = int(str_num[:mid]) % 10
        rev_num = str(upto_mid) + str_num[mid] + str(upto_mid)[::-1]
        
        # The logic below is same as even length number
        if number >= int(rev_num):
            # Get 124; reverse = "124" + "21"
            palin = str(int(str_num[:mid+1]) + 1)
            reverse = palin + palin[-2::-1]
            if len(reverse) > length:
                # 999 scenario
                reverse = reverse[:mid] + reverse[mid+1:]
            return reverse
        else:
            return rev_num
        

number = input("Enter a number: ")
print nextPalindrome(number)
