class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if not numbers:
            return []
        numbers.sort()
        res = []
        r = len(numbers) - 1
        for i in range(len(numbers)):
            l = i + 1
            temp = -numbers[i]
            while l < r:
                if numbers[l] + numbers[r] == temp:
                    res.append([numbers[i], numbers[l], numbers[r]])
                    while numbers[l+1] == numbers[l]:
                        l += 1
                    continue
                if numbers[l] + numbers[r] < temp:
                    l += 1
                    continue
                if numbers[l] + numbers[r] > temp:
                    r -= 1
                    continue
        return res
sol = Solution()
A = [-1, 0, 1]
print sol.threeSum(A)
