""" 139. Word Break - Medium
topic: dynamic programming
related: 140. Word Break II - Hard

Given a non-empty string s and a dictionary wordDict containing a list of non-empty
words, determine if s can be segmented into a space-separated sequence of one or
more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
 """


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        max_word_len = len(max(wordDict, key=len))
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(1, min(i, max_word_len) + 1):
                if dp[i - j] and s[i - j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]


if __name__ == "__main__":
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(Solution().wordBreak(s, wordDict))
