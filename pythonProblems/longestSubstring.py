class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        wendow = s[0]
        curr = s[0]

        for j in range(1,len(s)):
            for i in range(j,len(s)):
                if s[i] not in curr:
                    curr += s[i]
                else:
                   
                    break
            if len(curr) > len(wendow):
                        wendow = curr
            curr = s[j]

        return wendow


check = Solution()
print(check.lengthOfLongestSubstring("abcabcbb")) 
print(check.lengthOfLongestSubstring("au"))     
print(check.lengthOfLongestSubstring("pwwkew"))   