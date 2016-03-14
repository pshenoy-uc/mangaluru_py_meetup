import pdb

def nextPalindrome(number):
    str_num = str(number)
    length = len(str_num)
    mid = length // 2
    if float(length) % 2 == 0:
        rev_num = str_num[:mid] + str_num[mid-1::-1]
        if number >= int(rev_num):
            palin = str(int(str_num[:mid]) + 1)
            reverse = palin + palin[::-1]
            return reverse
        else:
            return rev_num
    else:
        rev_num = str_num[:mid] + str_num[mid] + str_num[mid-1::-1]
        if number >= int(rev_num):
            palin = str(int(str_num[:mid+1]) + 1)
            reverse = palin + palin[-2::-1]
            return reverse
        else:
            return rev_num
        

number = input("Enter a number: ")
print nextPalindrome(number)
