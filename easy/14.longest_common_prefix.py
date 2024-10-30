from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(strs, key=len)
        lists = [list(word) for word in strs]
        prefix = ""
        for i in range(len(shortest_word)):
            letters = [word[i] for word in lists]
            letter_set = set(letters)
            if len(letter_set) == 1:
                prefix += letter_set.pop()
                i+=1
            else:
                return prefix

        return prefix


l = ["flower","flo","floght"]

print(Solution().longestCommonPrefix(l))