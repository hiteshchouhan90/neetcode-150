class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
             return False
        count_array = 26 * [0]
        for i in range(len(s)):
             count_array[ord(s[i]) - ord('a')] += 1
             count_array[ord(t[i]) - ord('a')] -= 1
        for i in count_array:
             if i != 0:
                  return False
        return True

