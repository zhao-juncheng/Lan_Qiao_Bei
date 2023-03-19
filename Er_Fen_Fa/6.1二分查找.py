def binary_search(nums,target):
    '''
    二分查找，在升序数组nums中，查找到target并返回target的索引值，若找不到，则返回 -1
    nums:List[int]
    target:int
    return:int
    '''
    n = len(nums)
    l,h = 0,n-1
    
    while l <= h:
        mid = l + ( h - l ) // 2
        if nums[mid] == target :
            return mid
        elif nums[mid] > target :
            h = mid - 1
        elif nums[mid] < target :
            l = mid + 1
    return -1

nums = [-1,0,3,5,9,12]
target = 5
nums=[1,3,5,6,7,8,9,10]
target=5
x = binary_search(nums,target)
print('target=',target,'nums=',nums)
print('nums[{0}] = {1}'.format(x,nums[x]))
