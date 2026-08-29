class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mem = defaultdict(list)
        
        for string in strs:
            mem[str(sorted(string))].append(string)
        
        return list(mem.values())