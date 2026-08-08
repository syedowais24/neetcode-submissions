class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # Create buckets where index represents the frequency
        freq = [[] for i in range(len(nums) + 1)]
        
        # Step 1: Count occurrences of each number
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        # Step 2: Group numbers by their frequency
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        # Step 3: Iterate backwards from highest possible frequency to 0
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
