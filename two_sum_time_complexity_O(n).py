class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        frequency={};
        index=[];
        for i in range(len(nums)):
            targe=target-nums[i];
            if targe in frequency:
                index.append(i);
                index.append(frequency[targe]);
            else:
                frequency[nums[i]]=i;
        return index;
