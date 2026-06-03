import collections

class Solution:
    def groupAnagrams(self, strs):
        # This special map automatically creates a new sublist [] for any new count signature
        anagram_map = collections.defaultdict(list)
        
        for word in strs:
            # 1. Take the count: Create an array of 26 zeros (one for each English letter)
            count = [0] * 26
            
            # Populate the count array for the current word
            for char in word:
                # ord() converts a letter to its ASCII number. 
                # ord(char) - ord('a') perfectly maps 'a' to index 0, 'b' to index 1, etc.
                count[ord(char) - ord('a')] += 1
                
            # 2. Convert the count array to a locked tuple so it can be a Hash Map key
            signature = tuple(count)
            
            # 3. Organize into a sublist: Append the original word to this specific count's list
            anagram_map[signature].append(word)
            
        # Return all the organized sublists
        return list(anagram_map.values())