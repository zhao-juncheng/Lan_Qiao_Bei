'''
81题
'''
class Solution:
    def search(self,nums,target):
        n=len(nums)
        h,r=0,n-1
        while h<=r:
            mid=h+(r-h)//2
            if nums[mid]==target:
                return True
            
        return False


a=Solution()
nums=[2,5,6,0,0,1,2]
target=6
print(a.search(nums,target))
