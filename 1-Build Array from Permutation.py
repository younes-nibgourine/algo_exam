class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[0]*len(nums)
        for i in range(len(nums)):
            ans[i]=nums[nums[i]]
        return ans
ob=Solution()
print(ob.buildArray([0,2,1,5,3,4]))