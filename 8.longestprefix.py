class Solution(object):
    def longestCommonPrefix(self, str):
        if not str:
            return ""

        s1 = min(str)
        s2 = max(str)
        i=0
        while i<len(s1) and i <len(s2) and s1[i]==s2[i]:
            i+=1
        return s1[:i]   