class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            flag = 1
            for j in range(len(words[i])):
                if words[i][j] not in allowed:
                    flag = 0
                    break
            if flag:
                count = count + 1
        return count
