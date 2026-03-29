class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char = set()
        maxLen = 0
        start = 0
        for i in range(len(s)):
            while s[i] in char:
                char.remove(s[start])
                start+=1

            char.add(s[i])
            maxLen = max(maxLen,i-start+1)  
        return maxLen          