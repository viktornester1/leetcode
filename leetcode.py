# Minimum Size Subarray Sum
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        right = 0
        left = 0
        result = 0

        sumOfCurrentWindow = 0
        while left != len(nums):  # ?
            temp_list = []
            while sum(temp_list) <= target:
                temp_list = nums[left:right+1]
                right += 1
            result = len(temp_list)
            print(f"List:   {temp_list}")
            print(f"Result: {result}")

            while sum(temp_list) >= target:
                left += 1




        return result


s = Solution()
prnt = s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
print(prnt)
"""     
        ...   
        sumOfCurrentWindow = 0
        while left != len(nums):  # ?
            temp_list = []
            while sum(temp_list) <= target:
                temp_list.append(nums[right])
                right += 1
            result = len(temp_list)
            print(temp_list)

            while sum(temp_list) >= target:
                pass
                


        return result
"""

# Minimum Rounds to Complete All Tasks
"""
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counts = dict()
        for task in tasks:
            if task not in counts:
                counts[task] = 0
            counts[task] += 1

        res = 0
        for key, val in counts.items():
            if val == 1:
                return -1
            elif val % 3 == 0:
                res += (val // 3)
            else:
                res += (val // 3) + 1

        return res
"""
# Find Nearest Point That Has the Same X or Y Coordinate
"""
from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        temp = 0
        temp1 = 0
        count = 0
        for i, sublist in enumerate(points):
            if sublist[0] == x:
                print("!!!!!!!!!!!!!!!!")
                temp = i
            elif sublist[1] == y:
                print("@@@@@@@@@@@@@@@@@")
                temp1 = i
            count += 1
            if temp != 0 or temp1 != 0:
                print("you lose?")
                return count

        return -1

        #  (sublist[1], sublist[2]) != (x, y):


s = Solution()

print(s.nearestValidPoint(3, 4, [[3, 4]]))"""
# Can Make Arithmetic Progression From Sequence
"""
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        return True
"""
# Largest Perimeter Triangle
"""
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            if nums[i - 2] + nums[i - 1] > nums[i]:
                return nums[i - 2] + nums[i - 1] + nums[i]
        return 0


solution = Solution()
result = solution.largestPerimeter([1, 2, 2])
print(result)
"""
# Subtract the Product and Sum of Digits of an Integer
"""class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        r1, r2 = 0, 1
        for i in str(n):
            r1 = r1 + int(i)
            r2 = r2 * int(i)
        return r2 - r1
        # доробити


solution = Solution()
result = solution.subtractProductAndSum(4421)
print(result)
"""
""" 
def subtractProductAndSum(self, n: int) -> int:
    while n > 0:
        dg = n % 10
        dg *= dg
        print(dg)
        n //= 10
"""
# Average Salary Excluding the Minimum and Maximum Salary
"""
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)
"""
"""
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        return sum(salary) / len(salary)
"""
# Count Odd Numbers in an Interval Range
"""
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low += 1
        if high % 2 == 0:
            high -= 1
        return (high - low) // 2 + 1


s = Solution()
result = s.countOdds(3, 7)
print(result)
"""
# Longest Palindromic Subsequence / finish later
"""class Solution:
    @staticmethod
    def longestPalindromeSubseq(self, s: str) -> int:
        return 2


print(Solution.longestPalindromeSubseq("dw", "bbbab"))
"""
"""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
"""
# Multiply Strings bad solution
"""
class Solution:
    @staticmethod
    def multiply(num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


print(Solution.multiply("2", "3"))
print(type(Solution.multiply("2", "3")))
"""
