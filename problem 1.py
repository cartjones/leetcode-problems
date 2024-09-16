# Leetcode problem 1
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # creating dictionary to check for complement
        num_check = {}

        # going through nums list and calculating the complement we need
        for i, num in enumerate(nums):
            complement = target - num
            
            # checking if we have the complement in the dictionary and returning value
            if complement in num_check:
                return [num_check[complement], i]

            num_check[num]=i

# testing our solution
test_solution = Solution()
test_case = [2,7,11,15]
target = 9
print(test_solution.twoSum(test_case, target))