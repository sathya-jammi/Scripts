class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [1] * n
        for i in range(len(nums)):
            #print(i)
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    #print("I:",i,"J:",j,"Output:",output)
                    output[i] = output[i] * nums[j]
        return(output)
solution = Solution()
print("Final Output",solution.productExceptSelf([1,2,3,4]))
print("Final Output",solution.productExceptSelf([-1,1,0,-3,3]))