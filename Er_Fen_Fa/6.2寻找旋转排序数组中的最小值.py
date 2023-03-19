'''
[1,2,3,4,5]--->[3,4,5,1,2]
'''

class solution:
    # 有序数组旋转之后，寻找最大值与最小值
    
    def findMin(self,nums):
        h,r = 0,len(nums)-1
        
        if nums[0] < nums[r] :
            nums.reverse()
        print(nums) # 序列已被改变，要注意python的引用机制
        
        while h <= r:
            mid = h + ( r - h ) // 2
            print(mid)
            if r == h:
                return nums[r]
            elif nums[mid]>nums[r]:
                h=mid+1
            elif nums[mid]<nums[r]:
                r = mid
        return -1

    def findMax(self,nums):
        h,r = 0,len(nums)-1
        
        if nums[0] < nums[r] :
            nums.reverse()
        print(nums)    
        while h <= r:
            mid = h + ( r - h ) // 2
            print(mid)
            if r == h:
                return nums[r]
            elif nums[mid]>nums[r]:
                r = mid
            elif nums[mid]<nums[r]:
                h = mid + 1
        return -1


            
a = solution()
#nums = [3,4,5,0,2]
#nums = [2,1,7,4,3]
#nums = [1,2,3,4,5,8]
nums = [8,6,5,3,2,1]  # 经过这四组数据的测试，即便是单调升序或降序的序列，该查找依旧适用

min = a.findMin(nums)
print("最小值为：",min)

#nums = [1,2,3,4,5,8]
nums = [8,6,5,3,2,1]
max = a.findMax(nums)
print("最大值为：",max)
