'''
69，题目：实现 int sqrt(int x)函数。计算并返回x的平方根，其中x是非负整数。

思路：
    题目解读，利用二分法来找到一个x，使x的平方约等于N，
            由于x和N在此处都是整数，因此，x 在升序数组里查找，则是尽可能找到最大的。
            即，二分查找中“最右满足条件”的情况。
    1、确定 x 的取值空间。可以推出，x的值最大也只是小于等于N，x_values=[1,N]。
    2、二分查找 目标x值。h 为x_values左边界指针，r 为x_values右边界指针。
        2.1、mid = h + (r-h) // 2
        2.2、若 mid 的平方 == N ，则找到了 N 的平方根，因此返回 mid 的值
        2.3、若x_values[mid]的平方小于 N 。则需要在x_values的右段继续查找，但也并
            不能直接排除该值，因此 h = mid 。
        2.4、若x_values[mid]的平方大于 N 。则需要在x_values的左段继续查找，该值是
            可以直接排除的，因此 r = mid - 1 。
        
    3、在二分法的“最右满足条件”的情况下，当查找空间只剩下两个数值的话，但在某些情况下
        算法会出现死循环。因此，还需在只剩两个数值的时候，直接退出循环，然后再对这两
        个数值挨个儿进行一次判断。
        例如：在这个算法中，若是不进行上述处理，当遇到 N=2，左边界 h=0 ,右边界 r = 2
            此时，该算法就会陷入死循环中。
'''

class Solution:
    def f(self, N):
        h,r = 0,N
        while h <= r :
            mid = h + (r-h) // 2
            print(h,r,mid)
            x = mid*mid
            if x == N :
                return mid
            if h == r or h+1 == r :
                break
            elif x < N :
                h = mid
            elif x > N :
                r = mid -1
        if r*r <= N :
            return r
        else :
            return h
        

F = Solution()
N = 81
print(F.f(N))
