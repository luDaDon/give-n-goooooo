class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        curr_sum = 0
        min_sub = float("inf")

        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum >= target:
                min_sub = min(min_sub, right - left + 1) #comparing the window size
                curr_sum -= nums[left] #substract the leftmost element from the current windows sum
                left += 1 #shrink the window

        return min_sub if min_sub != float("inf") else 0

        