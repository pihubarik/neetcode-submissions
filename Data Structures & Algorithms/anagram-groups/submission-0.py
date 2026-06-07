class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps={}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)    
            # key = ''.join(sorted(word))
            if key not in grps:
                grps[key] = []
            grps[key].append(word)

        return list(grps.values())        