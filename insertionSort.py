'''
插入排序
插入排序时间复杂度仍然是O(n^2),思路与冒泡排序、选择排序不同
插入排序 维持一个已经排好序的子列表
其位置始终在列表前部，然后逐步扩大前半部这个子列表直到全表
类似整理扑克牌的过程

第1趟：子列表仅包含第一个数据项，将第2个数据项作为"新项"插入到子列表的合适位置中-已排序子列表包含了2个数据项
第2趟：继续将第3个数据项跟前两个数据项比对，并移动比自身大的数据项，空出位置，插入到子列表中
经过n-1趟比对和插入，子列表扩展到全表，排序完成

插入排序的比对，主要用来寻找"新项"的插入位置
    最差情况：每趟都与子列表中所有项进行比对，总比对次数与冒泡排序相同，数量级O(n^2)
    最好情况：列表已经排好序时，每趟仅需1次比对，总次数是O(n)
移动操作仅包一次赋值，是交换的1/3，性能会比冒泡排序好一些
'''

def insertionSort(aList):
    for index in range(1,len(aList)):
        curValue = aList[index]     #新项/插入项
        position = index

        while position > 0 and aList[position-1] > curValue:
            aList[position] = aList[position-1]
            position = position-1

        aList[position] = curValue


aList = [2,87,93,6,12,73,8,19,7,46,98,1,7]
insertionSort(aList)
print(aList)
