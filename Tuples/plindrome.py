tuple1=(1,2,3,2,1)
def is_palindrome(tup):
    left=0
    right=len(tup)-1
    while left<right:
        if tup[left]!=tup[right]:
            return False
        left+=1
        right-=1
    return True
if is_palindrome(tuple1):
    print("The tuple is a palindrome")
else:
    print("The tuple is not a palindrome")