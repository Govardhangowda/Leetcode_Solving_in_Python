class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        targe=[];
        s=set(nums);
        for i in range(len(nums)):
            c=target-nums[i];
            if(c in s):
                ind=nums.index(c);
                if (ind!=i):
                    targe.append(i);
                    targe.append(ind);
                    return targe;
        return false

