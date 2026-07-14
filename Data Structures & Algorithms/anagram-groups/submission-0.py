from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        used = [False] * len(strs)

        for i in range(len(strs)):
            if used[i]:
                continue

            group = [strs[i]]
            used[i] = True

            for j in range(i + 1, len(strs)):
                if not used[j]:
                    if sorted(strs[i].lower()) == sorted(strs[j].lower()):
                        group.append(strs[j])
                        used[j] = True

            result.append(group)

        return result