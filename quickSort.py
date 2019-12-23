'''
快速排序
思路：分拣、分裂，再对每一部分做递归排序
    依据一个中间值，把数据表分为两半，一半为大于中间值，一半为小于中间值
    关键在于 分拣

快速排序的递归三要素：
基本结束条件：数据表仅有1个数据项，自然是排序好的
缩小规模：根据"中值"，将数据表分为两半，最好情况是相等规模的两半
调用自身：将两半分别调用自身进行排序(排序基本操作在分裂过程)

分裂数据表的目标：找到"中值" 的位置
分裂数据表的手段：
    设置左右标(left/right mark)
    左标向右移动，右标向左移动
        左标一直向右移动，碰到比中值大的就停止
        右标一直向左移动，碰到比中值小的就停止
        然后把左右标所指的数据项交换
    继续移动，直到左标移动到右标的右侧，停止移动，这时右标所指位置就是"中值"应处的位置，将中值和这个位置交换
    分裂完成，左半部比中值小，右半部比中值大
'''

def quickSort(aList):
    quickSortHelper(aList, 0, len(aList)-1)

# 指定快速排序从哪开始， 从哪结束
def quickSortHelper(aList, first, last):
    if first < last:    #基本结束条件
        splitPoint = partition(aList, first, last)  #分裂，求得分裂点
        quickSortHelper(aList, first, splitPoint-1) #递归调用
        quickSortHelper(aList, splitPoint+1, last)

def partition(aList, first, last):
    pivotValue = aList[first]  #选定中值

    #左右标初值
    leftMark = first+1
    rightMark = last

    done = False
    while not done:

        while leftMark <= rightMark and aList[leftMark] <= pivotValue:
            leftMark = leftMark+1       #向右移动左标

        while rightMark >= leftMark and aList[rightMark] >= pivotValue:
            rightMark = rightMark-1     #向左移动右标

        if rightMark < leftMark:    #两标相错就结束移动
            done = True
        else:   #左右标的值交换
            temp = aList[leftMark]
            aList[leftMark] = aList[rightMark]
            aList[rightMark] = temp

        temp = aList[first]
        aList[first] = aList[rightMark] #中值就位
        aList[rightMark] = temp

    return rightMark    #中值点/分裂点

aList = [2,87,93,6,12,73,8,19,7,46,98,1,7]
quickSort(aList)
print(aList)
