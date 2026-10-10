class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans=[]
        for i in range(len(nums)-1,-1,-1):
            ans.insert(0,nums[i]);
        for j in range(0, len(nums)):
            nums.append(ans[j])
        return nums;