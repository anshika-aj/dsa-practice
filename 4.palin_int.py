class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False

        orignal = x
        reverse = 0

        while x>0:
            last = x% 10
            reverse = (reverse*10) + last      
            x= x//10
        return orignal == reverse    