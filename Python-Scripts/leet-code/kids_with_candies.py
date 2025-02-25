class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        largest = max(candies)
        #print("Candies",candies)
        for i in candies:
            #print("Candies",i)
            if i+extraCandies >= largest:
                result.append(True)
            else:
                result.append(False)
        return result

solution = Solution()
#result = []
print(solution.kidsWithCandies([2,3,5,1,3], 10))
print(solution.kidsWithCandies([2,3,5,1,3], 11))