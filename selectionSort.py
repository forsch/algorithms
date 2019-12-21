'''
选择排序算法
    对冒泡排序进行了你改进，保留了其基本的多趟比对思路，每趟都使用当前最大项就位
    对交换进行缆消减，相比起冒泡排序进行多次交换，每次仅进行一次交换，记录最大项所在位置
    最后再跟本趟最后一项进行交换
    选择排序的时间复杂度比冒泡排序稍优
        比对次数不变，O(n^2)
        交换次数减少为为 O(n)
'''

def selectionSort(aList):
    for passNum in range(len(aList)-1,0,-1):
        posOfMax=0
        for location in range(1,passNum+1):
            if aList[location] > aList[posOfMax]:
                posOfMax = location

        temp = aList[passNum]
        aList[passNum] = aList[posOfMax]
        aList[posOfMax] = temp

aList = [2,87,93,6,12,73,8,19,7,46,98,1,7]
selectionSort(aList)
print(aList)
