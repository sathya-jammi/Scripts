class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #Find the two largest numbers in the array
        max_container = 0
        secondlarge = 0
        if len(height) == 0:
            return null
        if len(height) == 1:
            return height[0]

        for i in range(len(height)):
            if i==len(height):
                break
            for j in range(i + 1,len(height)):
                if max_container < (min(height[i],height[j])*(j-i)):
                    max_container = (min(height[i],height[j])*(j-i))
        return max_container

solution = Solution()
print(solution.maxArea([10]))