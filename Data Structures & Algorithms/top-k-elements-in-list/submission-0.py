from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = Counter(nums)
        # sorted_items= sorted(freq.items(), key = lambda x:x[1], reverse = True)
        # result = [item[0] for item in sorted_items[:k]]
        # return result

        freq = Counter(nums)                         # Step 1: Count frequency
        buckets = [[] for _ in range(len(nums) + 1)] # Step 2: Create buckets
    
    # Step 3: Put numbers into their frequency bucket
        for num, count in freq.items():
            buckets[count].append(num)
    
    # Step 4: Collect from right to left (most frequent first)
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:                 # Stop when k elements collected
                    return result


        