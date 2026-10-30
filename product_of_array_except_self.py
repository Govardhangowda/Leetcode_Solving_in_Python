class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        val1=1;
        value=1;
        dup=nums[:]
        for i in range(len(nums)):
            temp=dup[i];
            nums[i]=value;
            value*=temp;

        for j in range(len(nums)-1,-1,-1):
            tem=dup[j];
            nums[j]*=val1;
            val1 *= tem;

        
        return nums;
