# Challenge #1: Sum of All Even Numbers

# class Solution(object):
#     def sumOfEvens(self, nums):
#         even_sum = 0
        
#         for num in nums:
#             if num % 2 == 0:
#                 even_sum += num
            
#         return even_sum

# solution = Solution()
# nums = [1, 2, 3, 4, 5, 6]
# print(solution.sumOfEvens(nums))  # Expected output: 12

# Challenge #2: Count Occurrences of a Number in a List

# class Solution(object):
#     def countOccurrences(self, nums, target):
#         count = 0
        
#         for num in nums:
#             if num == target:
#                 count += 1
#         return count

# solution = Solution()
# nums = [1, 2, 2, 3, 4, 2]
# target = 2
# print(solution.countOccurrences(nums, target))  # Expected output: 3

# Challenge #3: Reverse a String

# class Solution(object):
#     def reverseString(self, s):
#         return s[::-1]

# # Test the function
# solution = Solution()
# s = "hello"
# print(solution.reverseString(s))  # Expected output: "olleh"

# Challenge #4: Find the Largest Element in an Array

# class Solution(object):
#     def findLargest(self, nums):
#         largest = nums[0]
#         for i in nums:
#             if i > largest:
#                 largest = i
#         return largest

# # Test the function
# solution = Solution()
# nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# print(solution.findLargest(nums))  # Expected output: 9

# Challenge #4: Find the Second Largest Element in an Array

# class Solution(object):
#     def findSecondLargest(self, nums):
#         largest = second_largest = float('-inf')
        
#         for num in nums:
#             if num > largest:
#                 second_largest = largest
#                 largest = num
#             elif num > second_largest and num != largest:
#                 second_largest = num
                
#         if second_largest == float('-inf'):
#             return None
#         return second_largest
            

# # Test the function
# solution = Solution()
# nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# print(solution.findSecondLargest(nums))  # Expected output: 6