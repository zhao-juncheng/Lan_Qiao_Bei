
def SelectionSort(A):
    for i in range(0,len(A)-1):
        #在区间i=(0,len(A)-1)上，先暂定A[i=0]为最小的元素，记录其下标为min
        min=i
        #从i后面的一位i+1开始，到最后一个元素的位置len(A)，
        #查找有没有比A[min]更小的元素
        for j in range(i+1,len(A)):
            #如果找到了，则用这个元素的下标更新min的值，
            #表示A[min]是区间(i+1,len(A))中最小的元素
            if A[j]<A[min]:
                min=j
        #将A[i]与A[min]位置互换
        swap(i,min)
        #print(A)

#对数组的两个元素进行位置互换
def swap(a,b):
    print('a===',a,'b===',b)
    c=A[a]
    A[a]=A[b]
    A[b]=c

A=[9,8,7,6,5,4,3,2,1,29,30,18,13,16]
#A=[89, 45, 68, 90, 29, 34, 17]
print(A)
SelectionSort(A)
print(A)

'''
#找到数组A中最小的元素，记录下他的位置作为函数的返回值
def find_min_index(A,a,b):
    return A.index(min(A))
'''
