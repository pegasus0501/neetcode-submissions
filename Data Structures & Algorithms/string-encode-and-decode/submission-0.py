class Solution:
    def encode(self, strs: list[str]) -> str:
        # Phase 1: Encode using Length + "#" + String
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        # Phase 2: Decode using a manual pointer scanner
        res = []
        i = 0
        
        while i < len(s):
            # 1. Scan forward from 'i' to find the delimiter '#'
            j = i
            while s[j] != "#":
                j += 1
                
            # 2. Extract the length number sitting between i and j
            length = int(s[i:j])
            
            # 3. Read the exact string based on the length
            # Start right after the '#' (j+1) and go exactly 'length' characters
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # 4. Jump 'i' forward to the start of the next encoded block
            i = j + 1 + length
            
        return res