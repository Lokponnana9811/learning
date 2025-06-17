def isPalindrome(x: int) -> bool:
    if x == int(str(abs(x))[::-1]):
        return True
    else:
        return False
    
inp_num = int(input("Please enter a number: "))
result = isPalindrome(inp_num)
print (f"The number {inp_num} is a palindrome: {result}")