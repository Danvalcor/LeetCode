class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        dict = {}
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        maxFreq = max(dict.values())
        return sum(maxFreq == n for n in dict.values())*maxFreq



test = [1,2,2,3,1,4]


print(Solution.maxFrequencyElements(Solution, test))



