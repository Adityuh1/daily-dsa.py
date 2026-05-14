class Solution(object):
    def isPalindrome(self, x):
        stri = str(x)
        newString = stri[::-1]
        if stri == newString:
            return True
        else:
            return False
        