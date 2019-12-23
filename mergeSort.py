'''
归并排序
    分治策略在排序中的应用
    递归算法，将数据表持续分裂为两半，对两半分别进行归并排序
    递归的基本结束条件：数据表仅有一个数据项
    缩小规模：将数据表分裂为相等的两半，规模减为原来的二分之一
    调用自身：将两半分别调用自身排序，然后将分别排好序的两半进行归并，得到排好序的数据表

    1.分裂
        对数复杂度O(log n)
    2.归并
        相对于分裂的每个部分，其所有数据项都会被比较和放置一次，线性复杂度O(n)
    综合考虑，每次分裂的部分都进行一次O(n)的数据项归并，总时间复杂度O(nlog n)

    归并排序使用缆额外1倍的存储空间用于归并
    在对特大数据集排序时需要考虑
'''

def mergeSort(aList):
    if len(aList) <= 1: #递归结束条件
        return aList

    # 分解问题，并递归调用
    middle = len(aList) // 2
    print(middle)
    left = mergeSort(aList[:middle])    #左半部排好序
    right = mergeSort(aList[middle:])   #右半部排好序

    # 合并左右半部，完成排序
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(right if right else left)
    return merged


'''
def mergeSort(aList):
    if len(aList) > 1:              #基本结束条件
        mid = len(aList) // 2
        leftHalf = aList[:mid]
        rightHalf = aList[mid:]

        mergeSort(leftHalf)         #递归调用
        mergeSort(rightHalf)

        i = j = k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:    #拉链式交错把左右半部从小到大归并到结果列表中
                aList[k] = leftHalf[i]
                i+=1
            else:
                aList[k] = rightHalf[j]
                j+=1
            k+=1
        print(mid)
        while i < len(leftHalf):        #归并左半部剩余项
            aList[k] = leftHalf[i]
            i+=1
            k+=1

        while j < len(rightHalf):      #归并右半部剩余项
            aList[k] = rightHalf[j]
            j+=1
            k+=1
'''

aList = [2,87,93,6,12,73,8,19,7,46,98,1,7]
aList = mergeSort(aList)
print(aList)



