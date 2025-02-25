class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        print("Word1:",word1,"Length of word1",len(word1))
        print("Word2:",word2,"Length of word2",len(word2))
        
        words3 = ""
        new_length = 0
        for i in range(len(word1)):
            print("I:",i)
            #words3 = words3 + word1[i]+ word2[i]
            print("Words3",words3)
            if i >= len(word1) or i >= len(word2) :
                #new_length = -2
                break
            else:
                words3 = words3 + word1[i] + word2[i]
            
        if len(word1) == len(word2):
            print("Final Words",words3,"New Length:",new_length)
        elif len(word1) > len(word2):
            diff = len(word2) - len(word1)
            words3 = words3 + word1[diff:]
        else:
            diff = len(word1) - len(word2)
            words3 = words3 + word2[diff:]
        return (words3)
    
solution = Solution()
result = solution.mergeAlternately("abc","pqr")
print(result)
        