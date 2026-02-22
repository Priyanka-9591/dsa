def find_max(nums):
    if len(nums) == 0:
        return None   # handle empty list
    
    max_num = nums[0]   # assume first element is largest
    
    for num in nums:
        if num > max_num:
            max_num = num
            
    return max_num


# Example usage
nums = [4, 2, 9, 1, 7]
print(find_max(nums))   # Output: 9\
