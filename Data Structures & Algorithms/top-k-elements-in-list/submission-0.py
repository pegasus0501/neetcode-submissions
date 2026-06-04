class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = {}

        for num in nums: 
            map[num] = map.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num,freq in map.items():
            buckets[freq].append(num)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result 

        