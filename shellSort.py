'''
谢尔排序
    插入排序比对次数，在最好情况下是O(n),发生在列表已是有序的情况下 -- 列表越接近有序，插入排序的比对次数就越少
    谢尔排序以插入排序为基础，对无序表进行"间隔"划分子列表，每个子列表都执行插入排序
    随着子列表的数量越来越少，无序表的整体越来越接近有序，从而减少整体排序的比对次数越
    最后一趟是标准的插入排序，由于前面几趟已经将列表处理到接近有序，这一趟仅需少数几次移动即可完成
    子列表的间隔一般从n/2开始，每趟倍增：n/4,n/8...直到1

    谢尔排序的时间复杂度介于O(n)和O(n^2)之间
    若将间隔保持在2^k-1(1、3、5、7、15、31...)，谢尔排序的时间复杂度约为O(n^3/2)
'''
def shellSort(aList):
    sublistCount = len(aList) // 2     #初始间隔设置为2
    interval = 2
    while sublistCount > 0:

        for startPosition in range(0, sublistCount+1, interval):
            print(startPosition, sublistCount)
            gapInsertionSort(aList, startPosition, sublistCount)

        print("After increments of size", sublistCount, "The list is", aList)

        sublistCount = sublistCount // 2    #间隔缩小
        interval += 2

def gapInsertionSort(aList, start, gap):
    for index in range(start+gap, len(aList), gap):
        curValue = aList[index]
        position = index

        while position >= gap and aList[position-gap] > aList[position]:
            aList[position] = aList[position-gap]
            position = position-gap

        aList[position] = curValue

aList = [2,87,93,6,12,73,8,19,7,46,98,1,7]
aList = shellSort(aList)
print(aList)
