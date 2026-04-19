from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in group_map:

                group_map[key] = []
            group_map[key].append(word)

        return list(group_map.values())


       
        